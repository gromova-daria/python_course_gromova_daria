"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/sliding-window-maximum/?envType=problem-list-v2&envId=array
"""


from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        n = len(nums)
        max_values = []
        dq = deque()

        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                max_values.append(nums[dq[0]])

        return max_values