"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/subarrays-with-k-different-integers/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(k: int) -> int:
            count = defaultdict(int)
            left = result = 0
            
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1
                
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                    
                result += right - left + 1
            
            return result

        return at_most_k(k) - at_most_k(k - 1)

        