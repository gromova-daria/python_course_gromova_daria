"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-case-permutation/description/
"""


class Solution:
    def letterCasePermutation(self, s: str):
        result = []

        def backtrack(index, path):
            if index == len(s):
                result.append("".join(path))
                return

            char = s[index]

            if char.isdigit():
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(char.lower())
                backtrack(index + 1, path)
                path.pop()

                path.append(char.upper())
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
