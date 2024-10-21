"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask |= (1 << i)
            found_prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            for prefix in found_prefixes:
                if prefix ^ candidate in found_prefixes:
                    max_xor = candidate
                    break
                    
        return max_xor  