"""BFS queue and recursive DFS over deterministic adjacency order."""
import json
from collections import deque

def bfs(graph, start, events=None):
    if start not in graph:
        raise KeyError(start)
    queue = deque([start])
    discovered = {start}
    visited = []
    while queue:
        current = queue.popleft()
        visited.append(current)
        if events is not None:
            events.append({"step": "bfs_visit", "node": current, "queue": list(queue), "visited": visited.copy()})
        for neighbor in graph[current]:
            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)
                if events is not None:
                    events.append({"step": "bfs_enqueue", "from": current, "node": neighbor,
                                   "queue": list(queue)})
    return visited

def dfs(graph, start, events=None):
    if start not in graph:
        raise KeyError(start)
    seen = set()
    visited = []
    def visit(node, depth):
        seen.add(node)
        visited.append(node)
        if events is not None:
            events.append({"step": "dfs_enter", "node": node, "depth": depth, "visited": visited.copy()})
        for neighbor in graph[node]:
            if neighbor not in seen:
                visit(neighbor, depth+1)
        if events is not None:
            events.append({"step": "dfs_return", "node": node, "depth": depth})
    visit(start, 0)
    return visited

def main():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    breadth, depth = [], []
    b, d = bfs(graph, "A", breadth), dfs(graph, "A", depth)
    print(" ".join(b)); print(" ".join(d))
    return {"input": graph, "events": breadth+depth, "bfs": b, "dfs": d}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
