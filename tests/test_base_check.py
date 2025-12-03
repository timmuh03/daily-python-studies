import pytest
from base_check.solution import Solution


@pytest.mark.parametrize("n, base, expected", [
        # (string, base, expected) → expected: True / False
        ("1010",      2,  True),   # Binary — valid
        ("123",       2,  False),  # Digit '3' not allowed in base 2
        ("ABC",      16,  True),   # Hex uppercase — valid
        ("abc",      16,  True),   # Hex lowercase — valid (case-insensitive)
        ("Zz",       36,  True),   # Base 36 max digits — valid
        ("9Z",       36,  True),   # Mixed digits — valid
        ("10",       10,  True),   # Classic decimal — valid
        ("0",        10,  True),   # Single zero — valid
        ("",         10,  False),  # Empty string — invalid
        ("G",        16,  False),  # 'G' not valid in base 16
        ("1A2B",     12,  True),   # Base 12 allows 0-9,A-B — valid
        ("1C",       12,  False),  # 'C' = 12 → not allowed in base 12
        ("deadbeef", 16,  True),   # Classic hex word — valid
        ("DEADBEEF", 16,  True),   # Uppercase — valid
        ("hello",    36,  True),   # Base 36 supports full alphabet
        ("12.3",     10,  False),  # Decimal point not allowed
        ("-",        10,  False),  # Negative sign not allowed
        ("  123  ",  10,  False),  # Whitespace not allowed
        ("10",        1,  False),  # Base must be >= 2
        ("10",       37,  False),  # Base must be <= 36
    ])

def test_base_check(n, base, expected):
    sol = Solution()
    result = sol.is_valid_number(n, base)
    assert result == expected, f"Failed for string:{n}, base:{base}"
    