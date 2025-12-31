"""
Docstring for problems.easy.RansomNote.solution
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = [0] * 26
        difference = 0
        for char in ransomNote:
            i = ord(char) - ord("a")
            if need[i] == 0:
                difference += 1
            need[i] += 1

        for char in magazine:
           i = ord(char) - ord("a")
           if need[i] > 0:
               need[i] -= 1
               if need[i] == 0:
                   difference -= 1
                   if difference == 0:
                       return True
        return difference == 0