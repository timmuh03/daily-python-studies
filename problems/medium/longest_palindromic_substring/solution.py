"""
Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_s = "*" + "*".join(s) + "*" # Makes so odd an even length palindromes are calculated the same way.
        radius = [0] * len(new_s) # Hold the palindrome radius of each char in transformed string
        max_index = 0
        max_radius = 0
        max_r = 0 # Max right index explored so far
        center_r = 0 # Center index of max_r


        def find_radius(center, base_radius): # Finds number of layers beyond base_radius that are a valid palindrome
            left = center - base_radius - 1 # First left check outside the base radius
            right = center + base_radius + 1 # First right check outside the base radius
            if left < 0 or right >= len(new_s):
                return 0
            if new_s[left] != new_s[right]:
                return 0
            
            return 1 + find_radius(center, base_radius + 1)

        for i in range(len(new_s)):
            if i >= max_r: # Outside rightmost palindrome | Exploring new territory
                cur_radius = 0
                radius[i] = find_radius(i, cur_radius)
            else: # Inside an explored palindrome so we have some info to work from
                mirror = 2 * center_r - i # Mirrored opposite based on center of current palindrome
                cur_radius = min(radius[mirror], max_r - i) # Radius[mirror] = cur_radius, but haven't seen past max_r so take min
                radius[i] = cur_radius + find_radius(i, cur_radius)
            
            if radius[i] > max_radius: # Found a bigger palindrome
                max_radius = radius[i]
                max_index = i

            if i + radius[i] > max_r: # Palindrome that reaches farthes right
                max_r = i + radius[i]
                center_r = i

        # Find the string of the largest palindrome and take out the '*'
        left = max_index - max_radius
        right = max_index + max_radius
        piece = new_s[left:right + 1]
        result = ''.join(char for char in piece if char != '*')

        return result