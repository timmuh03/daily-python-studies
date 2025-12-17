"""
Docstring for problems.guess-number.solution

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked 
(the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

 The guess API is already defined for you.
 def guess(num: int) -> int:
 
 @param num, your guess
 @return -1 if num is higher than the picked number
          1 if num is lower than the picked number
          otherwise return 0
"""


# This is just a placeholder function
def guess(num: int) -> int:
    raise NotImplementedError("guess API not implemented")

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
                
        raise ValueError("Number not found")
