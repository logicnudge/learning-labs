# 012 — Python == vs is: Same Value, Same Object?

**Watch the Short:** [Episode #012 on YouTube](https://www.youtube.com/shorts/6yix_ffkwVs)

**Learning Hub:** [Browse episode #012](https://logicnudge.github.io/#lesson-012)

**Level:** Beginner · **Format:** Predict-Run-Explain

## Predict

Why does a == b return True but a is b return False?

## Run

```powershell
python python/episodes/012-python-equality-identity/demo.py
```

Expected output:

```text
True
False
```

## Explain

Their contents compare equal, but they're distinct list objects.

**Mental model:** Distinguish equality from object identity without unsafe integer-interning demonstrations.

**Important nuance:** Don't use small integer/string interning as an identity lesson; use separately created mutable lists.

## Transfer challenge

Assign c = a and compare both c == a and c is a.

**Reference:** https://docs.python.org/3/reference/datamodel.html
