"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        best_range = float('inf')
        result = []

        while min_heap:
            current_min, list_index, element_index = heapq.heappop(min_heap)

            if current_max - current_min < best_range:
                best_range = current_max - current_min
                result = [current_min, current_max]

            if element_index + 1 == len(nums[list_index]):
                break

            next_value = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
            current_max = max(current_max, next_value)

        return result