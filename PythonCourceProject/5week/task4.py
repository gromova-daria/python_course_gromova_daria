"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/array-of-doubled-pairs/
"""


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True