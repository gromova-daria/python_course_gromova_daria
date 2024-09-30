"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=problem-list-v2&envId=string
"""


from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        indices = []

        for i in range(len(s) - total_length + 1):
            substring = s[i:i + total_length]
            seen_words = Counter()

            for j in range(0, total_length, word_length):
                word = substring[j:j + word_length]
                if word in word_count:
                    seen_words[word] += 1

                    if seen_words[word] > word_count[word]:
                        break
                else:
                    break
            else:
                indices.append(i)

        return indices
