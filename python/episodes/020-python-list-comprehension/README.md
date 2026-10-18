# 020 — List Comprehension: Filter and Transform

**Level:** Beginner · **Format:** Two Paths, Same Result

## Predict

Which original values survive the even-number filter?

## Run

```powershell
python python/episodes/020-python-list-comprehension/demo.py
```

Expected output:

```text
[4, 16]
[4, 16]
```

## Explain

2 and 4; their squares are 4 and 16.

**Mental model:** Compare a filtered list comprehension with the equivalent loop.

**Important nuance:** Comprehensions do not replace every loop. Use an ordinary loop when readability or multiple effects matter.

## Transfer challenge

Change the predicate to n % 2 != 0 and predict the result.

**Reference:** https://docs.python.org/3/tutorial/datastructures.html
