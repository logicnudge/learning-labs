# 030 — Memoization — Stop Repeating Fibonacci

**Series:** DSA Explained Visually · **Status:** Runnable lesson; video not yet published

**Learning Hub:** [Explore lesson #030](https://logicnudge.github.io/#lesson-030)

## Predict

Why calculate the same Fibonacci value more than once?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/030-dp-memoization/demo.py
```

Expected printed output:

```text
8
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/030-dp-memoization/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Cache the result of each subproblem and reuse it.

Overlapping subproblems turn the recursion tree into a dependency DAG; keep cache hits separate from computations.

**Complexity:** O(n) time and O(n) memo/call-stack space for n >= 0 (excluding trace logging).

## Try a change

How many different values must be computed for fib(7) using memoization?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://docs.python.org/3/library/functools.html#functools.cache

**Video status:** Not yet published. The Watch link will be added only after a verified public Short exists.
