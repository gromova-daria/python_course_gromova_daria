"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator/?envType=problem-list-v2&envId=string
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "+":
                result += sign * num
                num = 0
                sign = 1
            elif char == "-":
                result += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        if num != 0:
            result += sign * num

        return result
