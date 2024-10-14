"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/shortest-palindrome/description/
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        rev_s = s[::-1]
        combined = s + "#" + rev_s

        n = len(combined)
        lps = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j

        longest_palindrome_length = lps[-1]

        chars_to_add = rev_s[: len(s) - longest_palindrome_length]

        return chars_to_add + s
