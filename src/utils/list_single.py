from __future__ import annotations
from typing import Iterable, Optional


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val})"
    

def build_list(values: Iterable[int]) -> ListNode | None:
    it = iter(values)
    try:
        first = next(it)
    except StopIteration:
        return None
    
    head = ListNode(first)
    tail = head

    for v in it:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def to_list(head: ListNode | None) -> list[int]:

    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out