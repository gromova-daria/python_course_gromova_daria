"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        n = len(cardPoints)
        if k >= n:
            return total_points
        
        min_window_sum = float('inf')
        current_window_sum = sum(cardPoints[:n - k])
        
        for i in range(n - k, n):
            min_window_sum = min(min_window_sum, current_window_sum)
            if i < n - 1:
                current_window_sum += cardPoints[i] - cardPoints[i - (n - k)]
        
        return total_points - min_window_sum