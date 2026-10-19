"""Find indices of a two-sum pair in one expected linear pass."""
import json

def two_sum(numbers, target, events=None):
    seen = {}  # value -> earliest observed index
    for index, value in enumerate(numbers):
        needed = target - value
        if events is not None:
            events.append({"step": "lookup", "index": index, "value": value, "needed": needed, "seen": {str(k): v for k, v in seen.items()}})
        if needed in seen:
            result = (seen[needed], index)
            if events is not None:
                events.append({"step": "found", "indices": list(result)})
            return result
        if value not in seen:
            seen[value] = index
            if events is not None:
                events.append({"step": "remember", "index": index, "value": value})
    if events is not None:
        events.append({"step": "not_found"})
    return None

def main():
    numbers = [2, 7, 11, 15]
    trace = []
    print(two_sum(numbers, 9, trace))
    return {"input": numbers, "target": 9, "events": trace, "result": [0, 1]}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
