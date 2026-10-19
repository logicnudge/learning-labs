# 025 — Stack — Matching Brackets

**Series:** DSA Explained Visually · **Status:** Runnable lesson; video not yet published

**Learning Hub:** [Explore lesson #025](https://logicnudge.github.io/#lesson-025)

## Predict

Why does ([)] fail even though it has matching bracket counts?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/025-valid-parentheses/demo.py
```

Expected printed output:

```text
True
False
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/025-valid-parentheses/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** The most recently opened bracket must close first.

A stack records unmatched opening brackets. Every closer must match the top, not just any opener.

**Complexity:** O(n) time and O(n) extra space in the worst case.

## Try a change

What does the algorithm return for an opening bracket that is never closed?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

**Video status:** Not yet published. The Watch link will be added only after a verified public Short exists.
