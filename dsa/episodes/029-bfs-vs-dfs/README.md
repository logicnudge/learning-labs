# 029 — BFS vs DFS — Different Visit Order

**Series:** DSA Explained Visually · **Status:** Runnable lesson; video not yet published

**Learning Hub:** [Explore lesson #029](https://logicnudge.github.io/#lesson-029)

## Predict

Why do two searches visit the same graph in different orders?

## Run the example

Python 3.10+; standard library only. From the root of `learning-labs`:

```sh
python dsa/episodes/029-bfs-vs-dfs/demo.py
```

Expected printed output:

```text
A B C D E
A B D C E
```

To inspect the generated, execution-derived steps, run:

```sh
python dsa/episodes/029-bfs-vs-dfs/demo.py --trace
```

The checked-in `trace.json` records the same executable trace and will be the reference for future animation. Instrumentation is excluded from the stated asymptotic auxiliary-space claims.

## Why it works

**Mental model:** BFS uses a FIFO queue; DFS follows one branch before backtracking.

With fixed neighbor order, BFS expands a level at a time; recursive DFS descends before exploring siblings. BFS shortest-edge paths apply to unweighted graphs.

**Complexity:** O(V + E) time and O(V) auxiliary space for adjacency-list graphs.

## Try a change

Add a cycle from E back to A. Why does neither traversal visit A twice?

Re-run the example after changing your own copy; keep the original demo unchanged when running repository tests.

## Correctness and limits

The worked example demonstrates this specific algorithm and assumptions, not every variant of the problem.

**Reference:** https://en.wikipedia.org/wiki/Graph_traversal

**Video status:** Not yet published. The Watch link will be added only after a verified public Short exists.
