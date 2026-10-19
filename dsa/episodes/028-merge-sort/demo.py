"""Stable merge sort, explicitly tracing splitting and front comparisons."""
import json

def merge_sort(values, events=None):
    def sort(items, depth):
        if len(items) <= 1:
            if events is not None:
                events.append({"step": "base", "depth": depth, "values": items.copy()})
            return items.copy()
        middle = len(items)//2
        if events is not None:
            events.append({"step": "split", "depth": depth, "values": items.copy(),
                           "left": items[:middle], "right": items[middle:]})
        left = sort(items[:middle], depth+1)
        right = sort(items[middle:], depth+1)
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            choose_left = left[i] <= right[j]  # ties keep original order
            if events is not None:
                events.append({"step": "compare", "depth": depth, "left": left[i],
                               "right": right[j], "take": "left" if choose_left else "right"})
            if choose_left:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        if events is not None:
            events.append({"step": "merged", "depth": depth, "values": merged.copy()})
        return merged
    return sort(list(values), 0)

def main():
    values = [7, 2, 5, 1]
    events = []
    answer = merge_sort(values, events)
    print(answer)
    return {"input": values, "events": events, "result": answer}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
