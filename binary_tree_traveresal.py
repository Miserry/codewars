# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# add root(1) to the stack
# go left, if left is None, remove 1 from the stack and add to a blank lst. Then look right.
# if left is True, add it on top of the stack.
# then look left again. If left is None, remove from stack.(add to blank lst)

# in our case below:
# step 1: stack = 1, look left.
# step 2: stack = 1, 2, look left.
# step 3: stack = 1, 2, 4, look left.
# step 4: look left = None. stack = 1, 2. lst = 4.
# step 5: look left = None. stack = 1. lst = 4......


#             1
#            / \
#           2   3
#          / \ / \
#         4  56   7


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        end_result = []
        stack = []

        while root or stack:     #while root is not null or stack is not empty: do stuff
                                 #so outer while will stop only when both root and stack return False - this means the root is null and your stack is []
            while root:
                stack.append(root)           #left is not None, so we append.
                root = root.left             #Looking left again, if it is not None while root will iterate, until it is None.
            root = stack.pop()               #We are out of while root, meaning Look.left is None. Remove the top from the stack.
            end_result.append(root.val)      #And add it to the end list.
            root = root.right                #Then look right, as left is None.

        return end_result
    
    
