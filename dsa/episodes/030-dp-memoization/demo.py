"""Memoized Fibonacci with visible computes and cache hits."""
import json

def fibonacci(n, events=None):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    memo = {0: 0, 1: 1}
    def visit(k):
        if k in memo:
            if events is not None:
                events.append({"step": "cache_hit", "n": k, "value": memo[k]})
            return memo[k]
        if events is not None:
            events.append({"step": "expand", "n": k})
        left = visit(k-1)
        right = visit(k-2)
        memo[k] = left+right
        if events is not None:
            events.append({"step": "compute", "n": k, "value": memo[k]})
        return memo[k]
    result = visit(n)
    if events is not None:
        events.append({"step": "done", "cache": {str(k): v for k,v in sorted(memo.items()) if k <= n}})
    return result

def main():
    events = []
    answer = fibonacci(6, events)
    print(answer)
    return {"input": 6, "events": events, "result": answer}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
