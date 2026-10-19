# 016 — Python List vs Tuple: What Can Change?

**Watch the Short:** [Episode #016 on YouTube](https://www.youtube.com/shorts/uVkWI0cLCLk)

**Learning Hub:** [Browse episode #016](https://logicnudge.github.io/#lesson-016)

**Level:** Beginner · **Format:** Bug Autopsy

## Predict

Can you call append on a tuple?

## Run

```powershell
python python/episodes/016-python-list-tuple/demo.py
```

Expected output:

```text
[1, 2, 3]
tuple has no append
```

## Explain

No, a tuple does not support append.

**Mental model:** Distinguish mutable lists from immutable tuples.

**Important nuance:** Tuple immutability does not make nested mutable objects immutable.

## Transfer challenge

Try putting a list inside a tuple; observe that the contained list can still mutate.

**Reference:** https://docs.python.org/3/reference/datamodel.html
