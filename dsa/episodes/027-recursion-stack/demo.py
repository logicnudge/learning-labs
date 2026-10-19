"""Factorial recursion with separate enter, base and return states."""
import json

def factorial(n, events=None):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    def visit(k):
        if events is not None:
            events.append({"step": "call", "n": k})
        if k <= 1:
            if events is not None:
                events.append({"step": "base", "n": k, "returns": 1})
            return 1
        child = visit(k-1)
        result = k * child
        if events is not None:
            events.append({"step": "return", "n": k, "child": child, "returns": result})
        return result
    return visit(n)

def main():
    events = []
    answer = factorial(4, events)
    print(answer)
    return {"input": 4, "events": events, "result": answer}

if __name__ == "__main__":
    import sys
    result = main()
    if "--trace" in sys.argv:
        print(json.dumps(result, indent=2))
