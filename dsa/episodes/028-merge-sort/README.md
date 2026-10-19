# 028 — Merge Sort — Split, Then Merge

**Series:** DSA Explained Visually · **Status:** Runnable lesson; video not yet published

**Learning Hub:** [Explore lesson #028](https://logicnudge.github.io/#lesson-028)

## Predict

Why split an unsorted list before ordering it?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/028-merge-sort/demo.py
```

Expected printed output:

```text
[1, 2, 5, 7]
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/028-merge-sort/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Sorted halves let us merge by comparing their fronts.

Split recursively until singleton lists, then repeatedly take the smaller front value when merging.

**Complexity:** O(n log n) time and O(n) auxiliary space for the shown implementation (excluding trace logging).

## Try a change

Try an already-sorted input and duplicates. Does the algorithm return a new list?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://en.wikipedia.org/wiki/Merge_sort

**Video status:** Not yet published. The Watch link will be added only after a verified public Short exists.
