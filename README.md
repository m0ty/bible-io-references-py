# bible-io-references-py

## Verse reference parsing

You can parse text references into `VerseRef` objects:

```python
from importlib import import_module

references = import_module("bible-io-references.references")

ref = references.VerseRef.from_str("John 3:16")
print(ref.book.full_name)  # John
print(ref.chapter)         # 3
print(ref.verse)           # 16
```

The parser currently accepts full book names (e.g. `John 3:16`) and enum abbreviations
(e.g. `jo 3:16`).

It also supports localized book names in Russian and Hebrew, for example:

- `Иоанна 3:16`
- `יוחנן 3:16`

It also accepts localized abbreviations (including common trailing-dot Russian style), for example:

- `Ин. 3:16`
- `יוח 3:16`


It now includes initial support for Spanish and Portuguese book names and abbreviations, for example:

- `Juan 3:16`
- `João 3:16`
- `Mat. 5:9`
- `Apoc 21:4`
