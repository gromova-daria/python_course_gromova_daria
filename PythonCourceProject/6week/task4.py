"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/grumpy-bookstore-owner/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
        max_extra = 0
        current_extra = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_extra += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_extra -= customers[i - minutes]
            max_extra = max(max_extra, current_extra)
        
        return total_satisfied + max_extra

        