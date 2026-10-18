# 018 — Python dict.get vs Square Brackets

**Level:** Beginner · **Format:** Bug Autopsy

## Predict

What does profile.get('role', 'guest') return?

## Run

```powershell
python python/episodes/018-python-dict-get/demo.py
```

Expected output:

```text
guest
KeyError
```

## Explain

guest

**Mental model:** Distinguish missing-key KeyError from .get default behavior.

**Important nuance:** .get() returns the default for missing keys, but may also return None when a present key maps to None.

## Transfer challenge

Set profile['role']='builder' and run both lookups again.

**Reference:** https://docs.python.org/3/tutorial/datastructures.html
