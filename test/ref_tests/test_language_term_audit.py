from src.bible_io_references.bible_book_enums import BibleBookEnum
from src.bible_io_references.languages import audit_language_terms


def _complete_term_table(prefix: str) -> dict[BibleBookEnum, tuple[str, ...]]:
    return {book: (f"{prefix}_{book.name}",) for book in BibleBookEnum}


def _build_minimal_complete_tables() -> tuple[
    dict[str, dict[BibleBookEnum, tuple[str, ...]]],
    dict[str, dict[BibleBookEnum, tuple[str, ...]]],
]:
    return {"xx": _complete_term_table("name")}, {"xx": _complete_term_table("abbr")}


def test_builtin_language_tables_have_no_blocking_quality_issues():
    report = audit_language_terms()

    assert report.collisions == ()
    assert report.empty_terms == ()
    assert report.non_canonical_whitespace_terms == ()
    assert report.missing_name_entries == ()
    assert report.missing_abbreviation_entries == ()
    assert not report.has_blocking_issues


def test_language_term_audit_detects_exact_duplicate_terms():
    names_by_language, abbreviations_by_language = _build_minimal_complete_tables()
    names_by_language["xx"][BibleBookEnum.Genesis] = ("dup_term", "dup_term")

    report = audit_language_terms(names_by_language, abbreviations_by_language)

    assert len(report.duplicate_terms) == 1
    issue = report.duplicate_terms[0]
    assert issue.language_code == "xx"
    assert issue.source == "names"
    assert issue.book == BibleBookEnum.Genesis
    assert issue.term == "dup_term"
    assert issue.occurrences == 2
    assert not report.has_blocking_issues


def test_language_term_audit_detects_cross_book_collisions_in_lookup_forms():
    names_by_language, abbreviations_by_language = _build_minimal_complete_tables()
    abbreviations_by_language["xx"][BibleBookEnum.Genesis] = ("A.B",)
    abbreviations_by_language["xx"][BibleBookEnum.Exodus] = ("AB",)

    report = audit_language_terms(names_by_language, abbreviations_by_language)

    assert report.has_blocking_issues
    assert any(issue.normalization == "no_period" for issue in report.collisions)
    assert any(issue.normalization == "compact" for issue in report.collisions)


def test_language_term_audit_detects_whitespace_and_missing_book_entries():
    names_by_language, abbreviations_by_language = _build_minimal_complete_tables()
    names_by_language["xx"][BibleBookEnum.Genesis] = ("  term   with   spaces  ",)
    del abbreviations_by_language["xx"][BibleBookEnum.John]

    report = audit_language_terms(names_by_language, abbreviations_by_language)

    assert len(report.non_canonical_whitespace_terms) == 1
    assert len(report.missing_abbreviation_entries) == 1
    assert report.has_blocking_issues
