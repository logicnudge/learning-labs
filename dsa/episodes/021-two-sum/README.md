# 021 — Two Sum — A Pair in One Pass

**Series:** DSA Explained Visually · **Status:** Runnable lesson and published video

**Learning Hub:** [Explore lesson #021](https://logicnudge.github.io/#lesson-021)

**Watch Short:** [YouTube #021](https://www.youtube.com/shorts/iTh5moe1KyY)

## Predict

Why can a hash map find two numbers without checking every pair?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/021-two-sum/demo.py
```

Expected printed output:

```text
(0, 1)
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/021-two-sum/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Two sum: use the missing complement.

Search a stored complement before remembering the current value. Every pair uses distinct indexes.

**Complexity:** Expected O(n) time, O(n) extra space using a hash table; worst-case hash operations depend on the implementation.

## Try a change

If the target is 6 and the input is [3, 3], why are two different positions required?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

**Video status:** Published on YouTube.
