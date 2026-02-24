import pytest
from problems.medium.design_circular_queue.solution import MyCircularQueue


# Script op formats:
# ("init", k)
# ("enQueue", value, expected_bool)
# ("deQueue", expected_bool)
# ("Front", expected_int)
# ("Rear", expected_int)
# ("isEmpty", expected_bool)
# ("isFull", expected_bool)


@pytest.mark.parametrize(
    "ops",
    [
        # Canonical example (matches the common LeetCode walkthrough)
        [
            ("init", 3),
            ("enQueue", 1, True),
            ("enQueue", 2, True),
            ("enQueue", 3, True),
            ("enQueue", 4, False),
            ("Rear", 3),
            ("isFull", True),
            ("deQueue", True),
            ("enQueue", 4, True),
            ("Rear", 4),
            ("Front", 2),
        ],
        # Empty behavior
        [
            ("init", 2),
            ("isEmpty", True),
            ("Front", -1),
            ("Rear", -1),
            ("deQueue", False),
            ("isFull", False),
        ],
        # Wrap-around behavior
        [
            ("init", 3),
            ("enQueue", 10, True),
            ("enQueue", 20, True),
            ("enQueue", 30, True),
            ("deQueue", True),
            ("deQueue", True),
            ("enQueue", 40, True),
            ("enQueue", 50, True),
            ("Front", 30),
            ("Rear", 50),
            ("isFull", True),
        ],
        # Rear wrap edge (rear index goes back to 0)
        [
            ("init", 2),
            ("enQueue", 1, True),
            ("enQueue", 2, True),
            ("deQueue", True),
            ("enQueue", 3, True),
            ("Rear", 3),
            ("Front", 2),
        ],
    ],
)
def test_circular_queue_scripts(ops):
    q = None

    for op in ops:
        op_name = op[0]

        if op_name == "init":
            _, k = op
            q = MyCircularQueue(k)

        elif op_name == "enQueue":
            assert q is not None, "Queue must be initialized before enQueue"
            _, value, expected = op
            got = q.enQueue(value)
            assert got == expected

        elif op_name == "deQueue":
            assert q is not None, "Queue must be initialized before deQueue"
            _, expected = op
            got = q.deQueue()
            assert got == expected

        elif op_name == "Front":
            assert q is not None, "Queue must be initialized before Front"
            _, expected = op
            got = q.Front()
            assert got == expected

        elif op_name == "Rear":
            assert q is not None, "Queue must be initialized before Rear"
            _, expected = op
            got = q.Rear()
            assert got == expected

        elif op_name == "isEmpty":
            assert q is not None, "Queue must be initialized before isEmpty"
            _, expected = op
            got = q.isEmpty()
            assert got == expected

        elif op_name == "isFull":
            assert q is not None, "Queue must be initialized before isFull"
            _, expected = op
            got = q.isFull()
            assert got == expected

        else:
            pytest.fail(f"Unknown op: {op}")