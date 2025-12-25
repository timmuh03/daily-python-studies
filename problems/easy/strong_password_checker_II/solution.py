"""
Docstring for problems.strong_password_checker_II.solution
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.
"""

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        has_double = False
        
        for i in range(len(password)):
            char = password[i]
            
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if char in "!@#$%^&*()-+":
                has_special = True            
        
            if i < len(password) - 1 and char == password[i +1]:
                has_double = True
            
        if has_upper and has_lower and has_digit and has_special and not has_double:
            return True
        
        return False