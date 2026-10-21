# Logic Nudge — Learning Labs

**Learn to predict. See the concept. Verify the code. Experiment. Build.**

These are independently reproducible, learner-facing resources, prepared for publishing before their related social videos. Code can be practiced even when an episode has not been released on YouTube.

## Python foundations (#011–#020)

Requirements: Python 3.10 or newer. No external packages, services or paid accounts.

From the root of this repository:

```shell
python python/episodes/011-python-list-references/demo.py
python -m unittest discover -s python/tests -v
```

You can also visit each numbered lesson below to read the explanation, expected output, and a small challenge.

- **#011** [Why Did a Change When We Edited b?](python/episodes/011-python-list-references/README.md) · [Watch Short](https://www.youtube.com/shorts/Uds_93JJsmA)
- **#012** [Python == vs is: Same Value, Same Object?](python/episodes/012-python-equality-identity/README.md) · [Watch Short](https://www.youtube.com/shorts/6yix_ffkwVs)
- **#013** [Python Negative Indexes Explained Visually](python/episodes/013-python-negative-indexing/README.md) · [Watch Short](https://www.youtube.com/shorts/6G-IxA4HNKA)
- **#014** [Why range(5) Stops at Four](python/episodes/014-python-range-stop/README.md) · [Watch Short](https://www.youtube.com/shorts/DkFhTjA3fCU)
- **#015** [Python Slicing: The Right Edge Is Excluded](python/episodes/015-python-slicing/README.md) · [Watch Short](https://www.youtube.com/shorts/AxMMbM9VSTA)
- **#016** [Python List vs Tuple: What Can Change?](python/episodes/016-python-list-tuple/README.md) · [Watch Short](https://www.youtube.com/shorts/uVkWI0cLCLk)
- **#017** [Python Truthiness Is Not the Same as Equality](python/episodes/017-python-truthiness/README.md) · [Watch Short](https://www.youtube.com/shorts/G9JLQGHW5EQ)
- **#018** [Python dict.get vs Square Brackets](python/episodes/018-python-dict-get/README.md) · [Watch Short](https://www.youtube.com/shorts/VJHmOe9Pjcw)
- **#019** [Python enumerate: Position Plus Value](python/episodes/019-python-enumerate/README.md) · [Watch Short](https://www.youtube.com/shorts/d7RqgjVr0TM)
- **#020** [List Comprehension: Filter and Transform](python/episodes/020-python-list-comprehension/README.md) · [Watch Short](https://www.youtube.com/shorts/cZg1H5wextk)

### Interactive practice

[Python #011 — Reference TraceLab](labs/python/011-reference-lab.html). Download/open the HTML locally to experiment; no server needed.

## DSA Explained Visually (#021–#030)

Ten runnable, language-independent algorithm lessons with Python 3.10+ implementations, executable traces and edge-case tests. **All ten DSA Shorts are published**; each lesson below links to its video.

Run from the repository root:

```shell
python dsa/episodes/021-two-sum/demo.py
python -m unittest discover -s dsa/tests -v
```

Explore the [complete DSA collection](dsa/README.md), or choose a lesson:

- **#021** [Two Sum — One-Pass Hashing](dsa/episodes/021-two-sum/README.md) · [Watch Short](https://www.youtube.com/shorts/iTh5moe1KyY)
- **#022** [Binary Search — Discard Half](dsa/episodes/022-binary-search/README.md) · [Watch Short](https://www.youtube.com/shorts/92BvQhiP9ME)
- **#023** [Two Pointers — Sorted Pair Search](dsa/episodes/023-two-pointers/README.md) · [Watch Short](https://www.youtube.com/shorts/ADHIwMfs28U)
- **#024** [Sliding Window — Reuse the Sum](dsa/episodes/024-sliding-window/README.md) · [Watch Short](https://www.youtube.com/shorts/FOGqDHmNVI4)
- **#025** [Stack — Valid Parentheses](dsa/episodes/025-valid-parentheses/README.md) · [Watch Short](https://www.youtube.com/shorts/Ki73mfgwCd4)
- **#026** [Reverse a Linked List — Save Next](dsa/episodes/026-reverse-linked-list/README.md) · [Watch Short](https://www.youtube.com/shorts/9eJxwVaYxx8)
- **#027** [Recursion — Calls and Returns](dsa/episodes/027-recursion-stack/README.md) · [Watch Short](https://www.youtube.com/shorts/yCLw9M-K4e4)
- **#028** [Merge Sort — Divide and Merge](dsa/episodes/028-merge-sort/README.md) · [Watch Short](https://www.youtube.com/shorts/7VuBVdaqsvQ)
- **#029** [BFS vs DFS — Traversal Order](dsa/episodes/029-bfs-vs-dfs/README.md) · [Watch Short](https://www.youtube.com/shorts/h_PaiiPWhfA)
- **#030** [Dynamic Programming — Memoization](dsa/episodes/030-dp-memoization/README.md) · [Watch Short](https://www.youtube.com/shorts/XaqwH3Bh0Eo)

## Educational integrity

Examples are checked against their recorded outputs. Editorial drafts, voice assets and internal production notes are intentionally excluded from this public repository. Some Python behavior depends on version or execution environment; refer to the caveats in each lesson. If you find a discrepancy, open an issue with the example, observed result, and Python version.

## Watch the companion content

[Logic Nudge on YouTube](https://www.youtube.com/@logicnudge). All ten Python foundations episodes link to their verified published Shorts. All ten DSA Shorts have Watch links alongside their code lessons. Browse the complete 30-lesson library in the [Logic Nudge Learning Hub](https://logicnudge.github.io/).

## License and privacy

Code and written lessons in this repository are available under [MIT](LICENSE). No personal learner data is collected by the static TraceLab exercise. Narrated audiovisual content is separate and not covered by this code license.
