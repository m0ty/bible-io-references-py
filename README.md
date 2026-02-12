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
