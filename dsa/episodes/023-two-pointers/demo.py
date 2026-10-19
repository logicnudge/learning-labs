"""Find a two-sum pair in a sorted list using opposing pointers."""
import json

def two_pointers(values, target, events=None):
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if events is not None:
            events.append({"step": "compare", "left": left, "right": right, "sum": total})
        if total == target:
            if events is not None:
                events.append({"step": "found", "indices": [left, right]})
            return (left, right)
        if total < target:
            left += 1
            move = "left_pointer_right"
        else:
            right -= 1
            move = "right_pointer_left"
        if events is not None:
            events.append({"step": "move", "which": move, "left": left, "right": right})
    if events is not None:
        events.append({"step": "not_found"})
    return None

def main():
    values = [1, 2, 4, 6, 9]
    events = []
    answer = two_pointers(values, 8, events)
    print(answer)
    return {"input": values, "target": 8, "events": events, "result": list(answer)}

if __name__ == "__main__":
    import sys
    result = main()
    if "--trace" in sys.argv:
        print(json.dumps(result, indent=2))
