"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/remove-duplicate-letters/?envType=problem-list-v2&envId=string
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)
