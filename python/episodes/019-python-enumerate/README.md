# 019 — Python enumerate: Position Plus Value

**Level:** Beginner · **Format:** State Lens

## Predict

What number is paired with A when start=1?

## Run

```powershell
python python/episodes/019-python-enumerate/demo.py
```

Expected output:

```text
1 A
2 B
3 C
```

## Explain

1

**Mental model:** Pair sequence values with indexes, including a configurable start.

**Important nuance:** enumerate tracks an index counter; it doesn't modify the input sequence.

## Transfer challenge

Remove start=1; what numbers appear?

**Reference:** https://docs.python.org/3/tutorial/datastructures.html
