"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)
