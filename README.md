# bible-io-references-py

Parse Bible verse references into structured Python objects.

## What this package supports

- Parsing a single verse reference into a `VerseRef`:
  - `John 3:16`
  - `jo 3:16` (enum abbreviation)
- Parsing a verse range into a `VerseRangeRef`:
  - `John 3:16-17`
  - `John 3:16-4:1` (same book, different chapter)
  - `John 3:16-Acts 1:2` (cross-book range)
- Flexible separators and spacing:
  - chapter/verse separator can be `:` or `.`
  - range separator can be hyphen, en dash, or em dash
  - extra surrounding whitespace is tolerated
- Book name matching from:
  - English full names (for all enum books)
  - enum abbreviations (for all enum books)
  - localized names and abbreviations for:
    - Arabic (`ar`)
    - Chinese (`zh`)
    - French (`fr`)
    - German (`de`)
    - Hebrew (`he`)
    - Hindi (`hi`)
    - Indonesian (`id`)
    - Korean (`ko`)
    - Portuguese (`pt`)
    - Russian (`ru`)
    - Spanish (`es`)
    - Tagalog (`tl`)

## Installation

```bash
pip install bible-io-references
```

## Usage

### Parse a single verse

```python
from bible_io_references import VerseRef

ref = VerseRef.from_str("John 3:16")
print(ref.book.full_name)  # John
print(ref.chapter)         # 3
print(ref.verse)           # 16
print(str(ref))            # John 3:16
```

### Parse a verse range

```python
from bible_io_references import VerseRangeRef

rng = VerseRangeRef.from_str("John 3:16-4:1")
print(rng.start.book.full_name, rng.start.chapter, rng.start.verse)  # John 3 16
print(rng.end.book.full_name, rng.end.chapter, rng.end.verse)        # John 4 1
print(str(rng))                                                       # John 3:16-4:1
```

### Parse either type with one helper

```python
from bible_io_references import VerseRangeRef, VerseRef, parse_reference

parsed = parse_reference("John 3:16-17")

if isinstance(parsed, VerseRangeRef):
    print(parsed.start, parsed.end)
elif isinstance(parsed, VerseRef):
    print(parsed)
```

### Parse localized references

```python
from bible_io_references import BibleLanguageEnum, VerseRef

print(VerseRef.from_str("Juan 3:16"))
print(VerseRef.from_str("Mat. 5:9", language=BibleLanguageEnum.SPANISH))
```

To restrict parsing to a specific language (to avoid cross-language abbreviation collisions),
pass a language enum. The default is `AUTO`, which searches all supported languages.

### AUTO-mode precedence and collision diagnostics

```python
from bible_io_references.references import AUTO_LANGUAGE_COLLISIONS, AUTO_LANGUAGE_PRECEDENCE

print(AUTO_LANGUAGE_PRECEDENCE)
print(AUTO_LANGUAGE_COLLISIONS.get("jn"))
```

In `AUTO` mode, English terms are checked first. Localized terms are then resolved using
`AUTO_LANGUAGE_PRECEDENCE` order.

### Audit language term tables (maintainers)

```python
from bible_io_references.languages import audit_language_terms

report = audit_language_terms()
print(report.has_blocking_issues)
print(len(report.duplicate_terms))
```

## Error handling

Invalid references raise `ParseVerseRefError`.

```python
from bible_io_references import ParseVerseRefError, VerseRef

try:
    VerseRef.from_str("NotABook 3:16")
except ParseVerseRefError as exc:
    print(str(exc))      # invalid verse reference
    print(exc.code)      # machine-readable reason code
    print(exc.details)   # optional detail text
    print(exc.to_dict()) # {'code': '...', 'details': '...'}
```

## Core types

- `BibleBookEnum`: canonical Bible books (including Protestant, Catholic deuterocanonical, and Eastern Orthodox additions in the enum)
- `BibleLanguageEnum`: language strategy enum (`AUTO`, `es`, `he`, etc.)
- `VerseRef`: single verse (`book`, `chapter`, `verse`)
- `VerseRangeRef`: range with `start` and `end` `VerseRef`s
- `ParseVerseRefError`: parse failure exception with structured diagnostics (`code`, `details`)
