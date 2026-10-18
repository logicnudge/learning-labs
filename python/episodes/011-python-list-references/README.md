# 011 — Why Did a Change When We Edited b?

**Level:** Beginner · **Format:** State Lens / Predict-Run-Explain

## Predict

After b = a, does b.append(3) change a?

## Run

```powershell
python python/episodes/011-python-list-references/demo.py
```

Expected output:

```text
[1, 2, 3]
[1, 2]
```

## Explain

Yes: both names refer to the same list object.

**Mental model:** Explain name binding, shared references, mutation and copying lists.

**Important nuance:** An assignment binds a name to an object; it does not copy the object. list.copy() creates a shallow copy.

## Transfer challenge

Replace b = a with b = a.copy(), then mutate b. Explain the difference.

**Reference:** https://docs.python.org/3/library/copy.html

## Interactive practice

[Explore the Python reference TraceLab](../../../labs/python/011-reference-lab.html). This file runs offline after cloning the repository. On GitHub, select **Download raw file** to run it in your browser.
