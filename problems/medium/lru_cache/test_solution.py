# test_lru_cache.py
# Adjust the import to match your project layout.
# Examples:
#   from lru_cache import LRUCache
#   from solution import LRUCache
from problems.medium.lru_cache.solution import LRUCache


def _list_keys(cache: LRUCache) -> list[int]:
    """
    Traverse the internal doubly linked list from head -> tail (excluding sentinels)
    and return the keys in order from most-recent to least-recent.

    This assumes your cache exposes:
      - cache.head
      - cache.tail
      - each node has .key, .next, .prev
    """
    head = cache.head
    tail = cache.tail

    assert head is not None
    assert tail is not None
    assert head.next is not None
    assert tail.prev is not None

    keys: list[int] = []
    seen_ids: set[int] = set()

    cur = head.next
    while cur is not tail:
        assert cur is not None, "Hit None before reaching tail (broken next pointers)"
        # Cycle detection: if we revisit a node, pointers are corrupted.
        cur_id = id(cur)
        assert cur_id not in seen_ids, "Cycle detected in list traversal"
        seen_ids.add(cur_id)

        keys.append(cur.key)
        cur = cur.next

    return keys


def _assert_sentinels_wired(cache: LRUCache) -> None:
    """
    Basic sentinel invariants: head <-> first ... last <-> tail,
    including the empty-list case.
    """
    head = cache.head
    tail = cache.tail

    assert head.prev is None or head.prev is not tail, "Head.prev should not point into list"
    assert tail.next is None or tail.next is not head, "Tail.next should not point into list"

    assert head.next is not None, "Head.next should always exist (at least tail)"
    assert tail.prev is not None, "Tail.prev should always exist (at least head)"

    assert head.next.prev is head, "head.next.prev must point back to head"
    assert tail.prev.next is tail, "tail.prev.next must point forward to tail"


def _assert_dict_list_consistent(cache: LRUCache) -> None:
    """
    Dict and list should have exactly the same keys, and no duplicates in the list.
    """
    list_keys = _list_keys(cache)
    dict_keys = list(cache.nodes.keys())

    assert len(list_keys) == len(set(list_keys)), "Duplicate keys in list"
    assert set(list_keys) == set(dict_keys), "Dict keys and list keys differ"
    assert len(list_keys) == len(cache.nodes), "List node count != dict size"


def _assert_capacity_ok(cache: LRUCache) -> None:
    assert len(cache.nodes) <= cache.capacity, "Cache exceeded capacity"


def _assert_all_invariants(cache: LRUCache) -> None:
    _assert_sentinels_wired(cache)
    _assert_dict_list_consistent(cache)
    _assert_capacity_ok(cache)


def test_put_get_basic() -> None:
    c = LRUCache(2)
    c.put(1, 1)
    _assert_all_invariants(c)

    c.put(2, 2)
    _assert_all_invariants(c)

    assert c.get(1) == 1
    _assert_all_invariants(c)

    # After get(1), 1 should be most recent: order [1, 2]
    assert _list_keys(c) == [1, 2]


def test_eviction_lru_on_put() -> None:
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    _assert_all_invariants(c)

    # Insert 3; should evict 1 (LRU is 1 because 2 was inserted after 1)
    c.put(3, 3)
    _assert_all_invariants(c)

    assert c.get(1) == -1
    assert c.get(2) == 2
    assert c.get(3) == 3
    _assert_all_invariants(c)

    # Recency: after get(2) then get(3), order should end at [3, 2]
    assert _list_keys(c) == [3, 2]


def test_get_updates_recency_affects_eviction() -> None:
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    _assert_all_invariants(c)

    # Touch 1 so that 2 becomes LRU
    assert c.get(1) == 1
    _assert_all_invariants(c)
    assert _list_keys(c) == [1, 2]

    # Now inserting 3 should evict 2
    c.put(3, 3)
    _assert_all_invariants(c)

    assert c.get(2) == -1
    assert c.get(1) == 1
    assert c.get(3) == 3
    _assert_all_invariants(c)


def test_put_existing_key_updates_value_and_recency() -> None:
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    _assert_all_invariants(c)

    # Update 1: should change value and move 1 to MRU
    c.put(1, 10)
    _assert_all_invariants(c)

    assert c.get(1) == 10
    _assert_all_invariants(c)
    assert _list_keys(c)[0] == 1  # 1 is MRU

    # Insert 3: should evict 2 (since 1 was recently updated/touched)
    c.put(3, 3)
    _assert_all_invariants(c)

    assert c.get(2) == -1
    assert c.get(1) == 10
    assert c.get(3) == 3
    _assert_all_invariants(c)


def test_no_duplicate_nodes_for_same_key_after_updates() -> None:
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    _assert_all_invariants(c)

    # Repeated updates should not create extra list nodes
    for v in range(5):
        c.put(1, v)
        _assert_all_invariants(c)
        assert c.get(1) == v
        _assert_all_invariants(c)

    assert len(_list_keys(c)) == len(c.nodes) == 2


def test_stress_small_sequence_invariants() -> None:
    c = LRUCache(3)

    ops = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("put", 3, 3),
        ("get", 2, None),
        ("put", 4, 4),   # should evict 1 (unless your get moved something else)
        ("get", 3, None),
        ("put", 2, 20),  # update existing
        ("put", 5, 5),
        ("get", 4, None),
    ]

    for op, a, b in ops:
        if op == "put":
            c.put(a, b)
        else:
            _ = c.get(a)
        _assert_all_invariants(c)

    # Capacity must hold
    assert len(c.nodes) <= 3