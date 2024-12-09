"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/binary-tree-right-side-view/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            rightmost_value = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                rightmost_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(rightmost_value)
        return result
