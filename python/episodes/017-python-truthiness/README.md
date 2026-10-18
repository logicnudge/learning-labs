# 017 — Python Truthiness Is Not the Same as Equality

**Level:** Beginner · **Format:** Predict-Run-Explain

## Predict

Is bool('0') True or False?

## Run

```powershell
python python/episodes/017-python-truthiness/demo.py
```

Expected output:

```text
int False
NoneType False
str False
list False
str True
```

## Explain

True: it is a nonempty string.

**Mental model:** Distinguish truth testing of 0, None, empty collections and nonempty strings.

**Important nuance:** Falsy values are not interchangeable; 0, None, empty lists and empty strings differ in type and meaning.

## Transfer challenge

Test bool('False') and bool({}).

**Reference:** https://docs.python.org/3/library/functions.html
