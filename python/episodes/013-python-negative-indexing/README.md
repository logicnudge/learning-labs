# 013 — Python Negative Indexes Explained Visually

**Level:** Beginner · **Format:** See the Invisible

## Predict

What does colors[-2] return?

## Run

```powershell
python python/episodes/013-python-negative-indexing/demo.py
```

Expected output:

```text
blue
green
```

## Explain

green

**Mental model:** Read negative indexing from the end of a sequence.

**Important nuance:** Negative indexing does not wrap indefinitely; out-of-range indices raise IndexError.

## Transfer challenge

Try colors[-3]. Predict the value before running.

**Reference:** https://docs.python.org/3/tutorial/datastructures.html
