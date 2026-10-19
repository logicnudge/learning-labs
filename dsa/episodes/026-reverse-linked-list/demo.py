"""Reverse a singly linked list in place, saving next before rewiring."""
import json

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def make_list(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head

def to_values(head):
    answer = []
    while head is not None:
        answer.append(head.value)
        head = head.next
    return answer

def reverse_list(head, events=None):
    previous = None
    current = head
    while current is not None:
        saved_next = current.next
        if events is not None:
            events.append({"step": "save_next", "current": current.value,
                           "next": saved_next.value if saved_next else None,
                           "previous": previous.value if previous else None})
        current.next = previous
        if events is not None:
            events.append({"step": "reverse_link", "current": current.value,
                           "points_to": previous.value if previous else None})
        previous = current
        current = saved_next
        if events is not None:
            events.append({"step": "advance", "current": current.value if current else None,
                           "previous": previous.value})
    return previous

def main():
    original = [1, 2, 3]
    events = []
    answer = to_values(reverse_list(make_list(original), events))
    print(answer)
    return {"input": original, "events": events, "result": answer}

if __name__ == "__main__":
    import sys
    outcome = main()
    if "--trace" in sys.argv:
        print(json.dumps(outcome, indent=2))
