# 013 — Python Negative Indexes Explained Visually

**Watch the Short:** [Episode #013 on YouTube](https://www.youtube.com/shorts/6G-IxA4HNKA)

**Learning Hub:** [Browse episode #013](https://logicnudge.github.io/#lesson-013)

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
