"""Check matching brackets with a last-in-first-out stack."""
import json

PAIRS = {")": "(", "]": "[", "}": "{"}
OPENING = set(PAIRS.values())

def valid_brackets(expression, events=None):
    stack = []
    for index, token in enumerate(expression):
        if token in OPENING:
            stack.append(token)
            if events is not None:
                events.append({"step": "push", "index": index, "token": token, "stack": stack.copy()})
        elif token in PAIRS:
            top = stack[-1] if stack else None
            if events is not None:
                events.append({"step": "compare", "index": index, "closing": token, "top": top})
            if not stack or stack.pop() != PAIRS[token]:
                if events is not None:
                    events.append({"step": "reject", "index": index})
                return False
            if events is not None:
                events.append({"step": "pop", "index": index, "stack": stack.copy()})
        else:
            raise ValueError("only bracket characters are supported")
    if events is not None:
        events.append({"step": "done", "remaining": stack.copy()})
    return not stack

def main():
    valid = "{[()]}"
    invalid = "([)]"
    a, b = [], []
    result = (valid_brackets(valid, a), valid_brackets(invalid, b))
    print(result[0]); print(result[1])
    return {"examples": [{"input": valid, "events": a, "result": result[0]},
                         {"input": invalid, "events": b, "result": result[1]}]}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
