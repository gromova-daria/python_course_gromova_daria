"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/palindrome-pairs/
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        word_dict = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                if is_palindrome(left):
                    reversed_right = right[::-1]
                    if reversed_right in word_dict and word_dict[reversed_right] != i:
                        result.append([word_dict[reversed_right], i])
                if j < len(word) and is_palindrome(right):
                    reversed_left = left[::-1]
                    if reversed_left in word_dict and word_dict[reversed_left] != i:
                        result.append([i, word_dict[reversed_left]])

        return result   
