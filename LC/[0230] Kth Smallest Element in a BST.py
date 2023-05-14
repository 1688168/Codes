###############
# 20230514
###############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        * inorder traversal BST will produce sorted values
        """
        cnt=0
        kth_val=-1
        def kth(node):
            nonlocal cnt, kth_val
            if node is None: return
            if cnt > k: return
            kth(node.left)
            cnt += 1
            #print("kth_val: ", kth_val)
            if cnt == k:
               
                kth_val=node.val
                return
          
            kth(node.right)

        #print("calling kth")
        kth(root)
        return kth_val


################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt=0
        self.val=None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def kth(rt):
            if self.cnt==k:
                return

            if rt is None: return


            kth(rt.left)

            self.cnt += 1
            if self.cnt == k:
                self.val=rt.val
                return
            kth(rt.right)

        kth(root)

        return self.val 



################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt=0
        self.val=None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if self.cnt==k:
            return self.val

        if root is None: return None


        self.kthSmallest(root.left, k)

        self.cnt += 1
        if self.cnt == k:
            self.val=root.val
            return self.val
        self.kthSmallest(root.right, k)

        return self.val
