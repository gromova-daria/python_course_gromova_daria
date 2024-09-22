"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/special-binary-string/description/
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        special_substrings = []

        for j in range(len(s)):
            count += 1 if s[j] == '1' else -1
            if count == 0:
                inner = self.makeLargestSpecial(s[i + 1:j])
                special_substrings.append('1' + inner + '0')
                i = j + 1

        special_substrings.sort(reverse=True)
        return ''.join(special_substrings)
