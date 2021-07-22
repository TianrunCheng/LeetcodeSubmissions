// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def printTrace(trace: ['TreeNode']):
            res = []
            for node in trace:
                res.append(node.val)
            print(res)

        trace = []
        
        p_trace = []
        q_trace = []
        
        def find(root: 'TreeNode'):
            if root == None:
                return
            trace.append(root)
            if root == p:
                for x in trace:
                    p_trace.append(x)
            if root == q:
                for x in trace:
                    q_trace.append(x)
            find(root.left)
            find(root.right)
            trace.pop(-1)
            return

        
        find(root)

        
        # printTrace(p_trace)
        # printTrace(q_trace)
        i = 0
        ml = min(len(p_trace), len(q_trace))
        while(i < ml and p_trace[i] == q_trace[i]):
            i += 1 
        
        print(i)
        return p_trace[i-1]
            
            
            