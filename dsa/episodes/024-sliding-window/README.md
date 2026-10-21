# 024 — Sliding Window — Keep the Running Sum

**Series:** DSA Explained Visually · **Status:** Runnable lesson and published video

**Learning Hub:** [Explore lesson #024](https://logicnudge.github.io/#lesson-024)

**Watch Short:** [YouTube #024](https://www.youtube.com/shorts/FOGqDHmNVI4)

## Predict

Why add three numbers again after shifting the window by one?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/024-sliding-window/demo.py
```

Expected printed output:

```text
(9, 2)
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/024-sliding-window/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Subtract the leaving element, add the entering one.

A fixed-width window changes in only two places on each step; track current and best sums separately.

**Complexity:** O(n) time and O(1) extra space for fixed k; rejects k <= 0 or k > len(values).

## Try a change

Try width 2 and predict the best sum and the window positions.

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://www.geeksforgeeks.org/window-sliding-technique/

**Video status:** Published on YouTube.
