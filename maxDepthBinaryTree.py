class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Given a TreeNode object where the definition is: 
        # class TreeNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None
        # We are trying to find the maximum depth going from the root to a leaf
        if root == None: 
            return 0
        else:
            # I use recursively call both sides, and constantly compare the two
            # tree nodes while adding to the deph. 
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
