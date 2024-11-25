"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/longest-nice-subarray/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1
        current_mask = nums[0]
        
        for i in range(1, len(nums)):
            if current_mask & nums[i] == 0:
                current_length += 1
                current_mask |= nums[i]
            else:
                j = i - 1
                while j >= 0 and current_mask & nums[i] != 0:
                    current_mask ^= nums[j]
                    current_length -= 1
                    j -= 1
                current_length += 1
                current_mask |= nums[i]
            max_length = max(max_length, current_length)
        
        return max_length
