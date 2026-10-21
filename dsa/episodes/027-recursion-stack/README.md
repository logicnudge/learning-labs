# 027 — Recursion — Calls Down, Values Back

**Series:** DSA Explained Visually · **Status:** Runnable lesson and published video

**Learning Hub:** [Explore lesson #027](https://logicnudge.github.io/#lesson-027)

**Watch Short:** [YouTube #027](https://www.youtube.com/shorts/yCLw9M-K4e4)

## Predict

Why does factorial start returning only after reaching one?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/027-recursion-stack/demo.py
```

Expected printed output:

```text
24
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/027-recursion-stack/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Separate call descent from return unwinding.

The base case returns one; each waiting call multiplies the result as the stack unwinds.

**Complexity:** O(n) time and O(n) call-stack space; very large n can hit Python recursion limits.

## Try a change

Predict factorial(0). What would happen without a stopping condition?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://docs.python.org/3/tutorial/controlflow.html#defining-functions

**Video status:** Published on YouTube.
