'''
有关树结构的算法
包括树的类型：二叉树，二叉搜索树，完全二叉树，等等。
遍历的方式：（前中后）序遍历，最短路径，广度优先，深度优先，等等。
'''

'''
两棵二叉搜索树中的所有元素
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        
        def inorder(root1):
            if not root1:
                return
            if root1.left:
                inorder(root1.left)
            res.append(root1.val)
            if root1.right:
                inorder(root1.right)
            #这是将二叉搜索树中的值有序记录出来的递归函数
        
        inorder(root1)
        inorder(root2)
        return sorted(res)
## 先通过递归函数将两个二叉搜索树中的值取到一个列表中，再对列表进行排序，这是第一次遇到二叉搜索树。


'''
二叉树的中序遍历
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def digui (a):
            if a == None:
                return
            digui(a.left) 
            ans.append(a.val)
            digui(a.right)
        digui(root)
        return ans 
        #递归的方法 

        zhan[]