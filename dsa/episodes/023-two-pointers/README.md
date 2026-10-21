# 023 — Two Pointers — Meet in the Middle

**Series:** DSA Explained Visually · **Status:** Runnable lesson and published video

**Learning Hub:** [Explore lesson #023](https://logicnudge.github.io/#lesson-023)

**Watch Short:** [YouTube #023](https://www.youtube.com/shorts/ADHIwMfs28U)

## Predict

How do two arrows find a pair in a sorted list?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/023-two-pointers/demo.py
```

Expected printed output:

```text
(1, 3)
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/023-two-pointers/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Move the pointer that can change the sum in the right direction.

On ascending sorted data, a sum that is too small must increase the left value; one too large must decrease the right value.

**Complexity:** O(n) time and O(1) extra space (input already sorted).

## Try a change

Change the target to 20. Explain why no pair is returned.

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

Requires an ascending sorted input; this demo does not sort or validate order first.

**Reference:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

**Video status:** Published on YouTube.
