# 015 — Python Slicing: The Right Edge Is Excluded

**Watch the Short:** [Episode #015 on YouTube](https://www.youtube.com/shorts/AxMMbM9VSTA)

**Learning Hub:** [Browse episode #015](https://logicnudge.github.io/#lesson-015)

**Level:** Beginner · **Format:** See the Invisible

## Predict

Which letters are returned by letters[1:4]?

## Run

```powershell
python python/episodes/015-python-slicing/demo.py
```

Expected output:

```text
['b', 'c', 'd']
['e', 'd', 'c', 'b', 'a']
```

## Explain

b, c, d; index four is excluded.

**Mental model:** Understand start-inclusive, stop-exclusive slicing and reversal.

**Important nuance:** Slicing returns a new list for a list input; it does not mutate the original list.

## Transfer challenge

Predict letters[:2] and letters[2:].

**Reference:** https://docs.python.org/3/tutorial/datastructures.html
