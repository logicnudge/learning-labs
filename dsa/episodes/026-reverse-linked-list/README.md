# 026 — Linked List — Save the Next Pointer

**Series:** DSA Explained Visually · **Status:** Runnable lesson; video not yet published

**Learning Hub:** [Explore lesson #026](https://logicnudge.github.io/#lesson-026)

## Predict

What goes missing if a linked-list arrow is reversed too soon?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/026-reverse-linked-list/demo.py
```

Expected printed output:

```text
[3, 2, 1]
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/026-reverse-linked-list/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** Save next before changing the link.

Keep three references: previous, current and saved next. Reverse links one at a time without losing the remaining chain.

**Complexity:** O(n) time and O(1) auxiliary space (relink existing nodes; trace snapshots are instrumentation).

## Try a change

Trace a one-node list and an empty list. What do the head pointers become?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://leetcode.com/problems/reverse-linked-list/

**Video status:** Not yet published. The Watch link will be added only after a verified public Short exists.
