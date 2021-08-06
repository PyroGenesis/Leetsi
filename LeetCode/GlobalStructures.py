# Used for defining the global structures used throughout LeetCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children