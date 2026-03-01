# bible-io-references-py

Parse Bible verse references into structured Python objects.

## What this package supports

- Parsing a **single verse reference** into a `VerseRef`:
  - `John 3:16`
  - `jo 3:16` (enum abbreviation)
- Parsing a **verse range** into a `VerseRangeRef`:
  - `John 3:16-17`
  - `John 3:16–17` (en dash)
  - `John 3:16-4:1` (same book, different chapter)
  - `John 3:16-Acts 1:2` (cross-book range)
- Flexible separators and spacing:
  - chapter/verse separator can be `:` or `.`
  - range separator can be `-`, `–`, or `—`
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
from importlib import import_module

references = import_module("bible-io-references.references")

ref = references.VerseRef.from_str("John 3:16")
print(ref.book.full_name)  # John
print(ref.chapter)         # 3
print(ref.verse)           # 16
print(str(ref))            # John 3:16
```

### Parse a verse range

```python
from importlib import import_module

references = import_module("bible-io-references.references")

rng = references.VerseRangeRef.from_str("John 3:16-4:1")
print(rng.start.book.full_name, rng.start.chapter, rng.start.verse)  # John 3 16
print(rng.end.book.full_name, rng.end.chapter, rng.end.verse)        # John 4 1
print(str(rng))                                                       # John 3:16-4:1
```

### Parse localized references

```python
from importlib import import_module

references = import_module("bible-io-references.references")

print(references.VerseRef.from_str("Иоанна 3:16"))   # Russian
print(references.VerseRef.from_str("יוחנן 3:16"))    # Hebrew
print(references.VerseRef.from_str("Juan 3:16"))     # Spanish
print(references.VerseRef.from_str("João 3:16"))     # Portuguese
print(references.VerseRef.from_str("요한복음 3:16"))  # Korean
print(references.VerseRef.from_str("约翰福音 3:16"))   # Chinese
```

Localized abbreviations are also supported, including forms like `Ин. 3:16`, `יוח 3:16`, `Mat. 5:9`, `Apoc 21:4`, and `요 3:16`.

## Error handling

Invalid references raise `ParseVerseRefError`:

```python
from importlib import import_module

references = import_module("bible-io-references.references")

try:
    references.VerseRef.from_str("NotABook 3:16")
except references.ParseVerseRefError as exc:
    print(str(exc))  # invalid verse reference
```

## Core types

- `BibleBookEnum`: canonical Bible books (including Protestant, Catholic deuterocanonical, and Eastern Orthodox additions in the enum)
- `VerseRef`: single verse (`book`, `chapter`, `verse`)
- `VerseRangeRef`: range with `start` and `end` `VerseRef`s
- `ParseVerseRefError`: parse failure exception
