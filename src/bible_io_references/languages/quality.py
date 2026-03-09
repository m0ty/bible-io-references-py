from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, Mapping

from ..bible_book_enums import BibleBookEnum

LanguageTermTables = Mapping[str, Mapping[BibleBookEnum, Iterable[str]]]


@dataclass(frozen=True, slots=True)
class DuplicateLanguageTermIssue:
    """A raw term appears multiple times for the same book in one source table."""

    language_code: str
    source: str
    book: BibleBookEnum
    term: str
    occurrences: int


@dataclass(frozen=True, slots=True)
class LanguageTermCollisionIssue:
    """Two or more books resolve to the same normalized lookup key."""

    language_code: str
    normalization: str
    key: str
    books: tuple[BibleBookEnum, ...]


@dataclass(frozen=True, slots=True)
class EmptyLanguageTermIssue:
    """A term entry is empty after loading from a source table."""

    language_code: str
    source: str
    book: BibleBookEnum


@dataclass(frozen=True, slots=True)
class WhitespaceLanguageTermIssue:
    """A term has non-canonical whitespace and will be normalized at runtime."""

    language_code: str
    source: str
    book: BibleBookEnum
    term: str
    canonical_term: str


@dataclass(frozen=True, slots=True)
class MissingLanguageBookEntriesIssue:
    """A language table is missing one or more canonical books."""

    language_code: str
    source: str
    missing_books: tuple[BibleBookEnum, ...]


@dataclass(frozen=True, slots=True)
class LanguageTermAuditReport:
    """Aggregated results from language-term quality checks."""

    duplicate_terms: tuple[DuplicateLanguageTermIssue, ...]
    collisions: tuple[LanguageTermCollisionIssue, ...]
    empty_terms: tuple[EmptyLanguageTermIssue, ...]
    non_canonical_whitespace_terms: tuple[WhitespaceLanguageTermIssue, ...]
    missing_name_entries: tuple[MissingLanguageBookEntriesIssue, ...]
    missing_abbreviation_entries: tuple[MissingLanguageBookEntriesIssue, ...]

    @property
    def has_blocking_issues(self) -> bool:
        """Return whether collisions/coverage/normalization errors were found."""
        return bool(
            self.collisions
            or self.empty_terms
            or self.non_canonical_whitespace_terms
            or self.missing_name_entries
            or self.missing_abbreviation_entries
        )

    @property
    def has_any_issues(self) -> bool:
        """Return whether any issue category is non-empty."""
        return bool(self.has_blocking_issues or self.duplicate_terms)


def _canonical_whitespace(term: str) -> str:
    return " ".join(term.split())


def _lookup_forms(term: str) -> Dict[str, str]:
    normalized = _canonical_whitespace(term).casefold()
    no_period = normalized.replace(".", "")
    return {
        "direct": normalized,
        "no_period": no_period,
        "compact": no_period.replace(" ", ""),
    }


def audit_language_terms(
    names_by_language: LanguageTermTables | None = None,
    abbreviations_by_language: LanguageTermTables | None = None,
) -> LanguageTermAuditReport:
    """Audit language term tables for duplicates, collisions, and normalization gaps.

    Notes:
        - Duplicate terms are reported as non-blocking quality issues.
        - Collisions, empty terms, whitespace anomalies, and missing books are
          considered blocking issues because they can affect parser behavior.
    """
    if names_by_language is None:
        from . import BOOK_NAMES_BY_LANGUAGE

        names_by_language = BOOK_NAMES_BY_LANGUAGE
    if abbreviations_by_language is None:
        from . import BOOK_ABBREVIATIONS_BY_LANGUAGE

        abbreviations_by_language = BOOK_ABBREVIATIONS_BY_LANGUAGE

    duplicate_terms: list[DuplicateLanguageTermIssue] = []
    collisions: list[LanguageTermCollisionIssue] = []
    empty_terms: list[EmptyLanguageTermIssue] = []
    whitespace_terms: list[WhitespaceLanguageTermIssue] = []
    missing_name_entries: list[MissingLanguageBookEntriesIssue] = []
    missing_abbreviation_entries: list[MissingLanguageBookEntriesIssue] = []

    all_books = set(BibleBookEnum)
    all_languages = sorted(set(names_by_language) | set(abbreviations_by_language))

    for language_code in all_languages:
        names_for_language = names_by_language.get(language_code, {})
        abbreviations_for_language = abbreviations_by_language.get(language_code, {})

        missing_names = tuple(
            sorted(all_books - set(names_for_language), key=lambda book: book.name)
        )
        if missing_names:
            missing_name_entries.append(
                MissingLanguageBookEntriesIssue(
                    language_code=language_code,
                    source="names",
                    missing_books=missing_names,
                )
            )

        missing_abbreviations = tuple(
            sorted(all_books - set(abbreviations_for_language), key=lambda book: book.name)
        )
        if missing_abbreviations:
            missing_abbreviation_entries.append(
                MissingLanguageBookEntriesIssue(
                    language_code=language_code,
                    source="abbreviations",
                    missing_books=missing_abbreviations,
                )
            )

        for source_name, source_table in (
            ("names", names_for_language),
            ("abbreviations", abbreviations_for_language),
        ):
            for book, terms in source_table.items():
                term_counts: Dict[str, int] = defaultdict(int)

                for term in terms:
                    if term == "":
                        empty_terms.append(
                            EmptyLanguageTermIssue(
                                language_code=language_code,
                                source=source_name,
                                book=book,
                            )
                        )
                        continue

                    canonical = _canonical_whitespace(term)
                    if canonical != term:
                        whitespace_terms.append(
                            WhitespaceLanguageTermIssue(
                                language_code=language_code,
                                source=source_name,
                                book=book,
                                term=term,
                                canonical_term=canonical,
                            )
                        )

                    term_counts[term] += 1

                for raw_term, occurrences in term_counts.items():
                    if occurrences > 1:
                        duplicate_terms.append(
                            DuplicateLanguageTermIssue(
                                language_code=language_code,
                                source=source_name,
                                book=book,
                                term=raw_term,
                                occurrences=occurrences,
                            )
                        )

        collision_index: Dict[str, Dict[str, set[BibleBookEnum]]] = {
            "direct": defaultdict(set),
            "no_period": defaultdict(set),
            "compact": defaultdict(set),
        }

        for source_table in (names_for_language, abbreviations_for_language):
            for book, terms in source_table.items():
                for term in terms:
                    if term == "":
                        continue
                    for normalization, key in _lookup_forms(term).items():
                        collision_index[normalization][key].add(book)

        for normalization, entries in collision_index.items():
            for key, books in entries.items():
                if len(books) <= 1:
                    continue
                collisions.append(
                    LanguageTermCollisionIssue(
                        language_code=language_code,
                        normalization=normalization,
                        key=key,
                        books=tuple(sorted(books, key=lambda book: book.name)),
                    )
                )

    duplicate_terms.sort(
        key=lambda issue: (
            issue.language_code,
            issue.source,
            issue.book.name,
            issue.term,
        )
    )
    collisions.sort(
        key=lambda issue: (
            issue.language_code,
            issue.normalization,
            issue.key,
            tuple(book.name for book in issue.books),
        )
    )
    empty_terms.sort(
        key=lambda issue: (
            issue.language_code,
            issue.source,
            issue.book.name,
        )
    )
    whitespace_terms.sort(
        key=lambda issue: (
            issue.language_code,
            issue.source,
            issue.book.name,
            issue.term,
        )
    )
    missing_name_entries.sort(key=lambda issue: issue.language_code)
    missing_abbreviation_entries.sort(key=lambda issue: issue.language_code)

    return LanguageTermAuditReport(
        duplicate_terms=tuple(duplicate_terms),
        collisions=tuple(collisions),
        empty_terms=tuple(empty_terms),
        non_canonical_whitespace_terms=tuple(whitespace_terms),
        missing_name_entries=tuple(missing_name_entries),
        missing_abbreviation_entries=tuple(missing_abbreviation_entries),
    )
