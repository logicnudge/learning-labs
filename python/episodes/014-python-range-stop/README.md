# 014 — Why range(5) Stops at Four

**Watch the Short:** [Episode #014 on YouTube](https://www.youtube.com/shorts/DkFhTjA3fCU)

**Learning Hub:** [Browse episode #014](https://logicnudge.github.io/#lesson-014)

**Level:** Beginner · **Format:** Timeline / State Lens

## Predict

Is 10 included in range(2, 10, 3)?

## Run

```powershell
python python/episodes/014-python-range-stop/demo.py
```

Expected output:

```text
[0, 1, 2, 3, 4]
[2, 5, 8]
```

## Explain

No. The stop value is excluded.

**Mental model:** Understand start-inclusive, stop-exclusive ranges and step size.

**Important nuance:** range is a range object; list(range(...)) materializes its values for display.

## Transfer challenge

Predict list(range(1, 7, 2)).

**Reference:** https://docs.python.org/3/library/functions.html
