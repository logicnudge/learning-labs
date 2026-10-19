"""Maximum sum over contiguous windows of exactly k numbers."""
import json

def best_window(values, k, events=None):
    if not 1 <= k <= len(values):
        raise ValueError("k must be from 1 through len(values)")
    current = sum(values[:k])
    best = current
    best_start = 0
    if events is not None:
        events.append({"step": "initial", "start": 0, "end": k-1, "current": current, "best": best})
    for end in range(k, len(values)):
        leaving = values[end-k]
        entering = values[end]
        current = current - leaving + entering
        if current > best:
            best = current
            best_start = end-k+1
        if events is not None:
            events.append({"step": "slide", "start": end-k+1, "end": end,
                           "leaving": leaving, "entering": entering, "current": current, "best": best})
    return best, best_start

def main():
    values = [2, 1, 5, 1, 3, 2]
    events = []
    result = best_window(values, 3, events)
    print(result)
    return {"input": values, "window_size": 3, "events": events, "result": list(result)}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
