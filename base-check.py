'''
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z
'''


def is_valid_number(n, base):

    return n


if __name__ == "__main__":
    print("Base Validation — Test Cases\n")

    tests = [
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
    ]

    for s, base, expected in tests:
        result = is_valid_number(s, base)
        status = "PASS" if result == expected else "FAIL"
        print(f"{s:>12} in base {base:2} → {str(result):5} | Expected: {expected} [{status}]")