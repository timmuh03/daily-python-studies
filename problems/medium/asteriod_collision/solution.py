"""
Docstring for problems.medium.asteriod_collision.solution

We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""



class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        survivors: list[int] = []

        for a in asteroids:
            while a != 0 and survivors and survivors[-1] > 0 and a < 0:
                top = survivors[-1]

                if abs(top) < abs(a):
                    survivors.pop()
                elif abs(top) == abs(a):
                    survivors.pop()
                    a = 0
                    break
                elif abs(top) > abs(a):
                    a = 0
                    break

            if a != 0: survivors.append(a)

        return survivors


