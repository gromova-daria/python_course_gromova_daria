"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/delete-and-earn/
"""


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_num = max(count)
        dp = [0] * (max_num + 1)

        for num in range(1, max_num + 1):
            dp[num] = max(dp[num - 1], dp[num - 2] + num * count[num])

        return dp[max_num]       