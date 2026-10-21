# 022 — Binary Search — Discard Half

**Series:** DSA Explained Visually · **Status:** Runnable lesson and published video

**Learning Hub:** [Explore lesson #022](https://logicnudge.github.io/#lesson-022)

**Watch Short:** [YouTube #022](https://www.youtube.com/shorts/92BvQhiP9ME)

## Predict

How does one midpoint comparison eliminate half the list?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/022-binary-search/demo.py
```

Expected printed output:

```text
5
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/022-binary-search/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Sorted values let you reject an entire interval.

Maintain inclusive low/high bounds and discard only positions that cannot contain the target. Sorted input is required.

**Complexity:** O(log n) time and O(1) extra space for this iterative implementation.

## Try a change

What happens when 11 is absent from the sorted list? Trace each midpoint before returning -1.

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

Requires an ascending sorted input; this demo does not sort or validate order first.

**Reference:** https://docs.python.org/3/library/bisect.html

**Video status:** Published on YouTube.
