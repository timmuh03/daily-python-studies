"""
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""



class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        coin_sum:list = [0] * (amount + 1)

        for a in range(1, amount + 1):
            possibles = []

            for coin in coins:
                if coin > a:
                    continue
                if a == coin:
                    possibles.append(1)
                elif coin_sum[a - coin]:
                    possibles.append(coin_sum[a - coin] + 1)
            if possibles:
                coin_sum[a] = min(possibles)
            else:
                coin_sum[a] = None

        if coin_sum and coin_sum[-1]:
            return coin_sum[-1]
        else:
            return -1
