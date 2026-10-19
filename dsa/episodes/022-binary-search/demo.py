"""Binary search on sorted ascending values using inclusive bounds."""
import json

def binary_search(values, target, events=None):
    low, high = 0, len(values) - 1
    while low <= high:
        mid = low + (high - low) // 2
        value = values[mid]
        if events is not None:
            events.append({"step": "compare", "low": low, "mid": mid, "high": high, "value": value})
        if value == target:
            if events is not None:
                events.append({"step": "found", "index": mid})
            return mid
        if value < target:
            low = mid + 1
            move = "right"
        else:
            high = mid - 1
            move = "left"
        if events is not None:
            events.append({"step": "discard", "direction": move, "new_low": low, "new_high": high})
    if events is not None:
        events.append({"step": "not_found"})
    return -1

def main():
    values = [2, 4, 6, 8, 10, 12, 14]
    events = []
    index = binary_search(values, 12, events)
    print(index)
    return {"input": values, "target": 12, "events": events, "result": index}

if __name__ == "__main__":
    import sys
    result = main()
    if "--trace" in sys.argv:
        print(json.dumps(result, indent=2))
