"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            freq = {}
            for j in range(i, n):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1

                if any(v >= k for v in freq.values()):
                    count += 1

        return count

