// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
To map a recursive structure like a tree to a linear object of a string,
there are many ways.
To reconstruct a recursive structure (tree) from a linear object of a string,
unless we have predefined the meaning of each coordinate of string, 
(the leetCode serialization, filling up with Null), 
reconstruction with one pass of the string is impossible.

Qi's idea:
Example1:  "1(2,3(4,5))"
finding substrings for subtrees will make time complexity O(n* log n)
reconstruction: find deviding point, recursively construct with substring

Tia's idea:
Example1: "1l2lnrnbr3l4lnrnbr5lnrnbbb"
recording the full trace of a recursive traversal of tree
which uniquely defines a tree.
reconstruction: use a loop to reconstruct with the trace of traversal
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def recur(root: TreeNode):
            if root == None:
                res.append('n') # 'None'
                return
            res.append(str(root.val))
            res.append('l')  # 'Left'
            recur(root.left)
            res.append('r')  # 'Right'
            recur(root.right)
            res.append('b')  # 'Back'
            return
        
        recur(root)
        rString = ""
        for ele in res:
            rString = rString + ele
        
        return rString

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        data = list(data)
        
        # print(data)
        
        global curr
        curr = 0
        
        def getEle() -> str:
            global curr
            if data[curr] == 'n':
                curr += 1
                return 'n'
            if data[curr] == 'l':
                curr += 1
                return 'l'
            if data[curr] == 'r':
                curr += 1
                return 'r'
            if data[curr] == 'b':
                curr += 1
                return 'b'
            
            # read a number, move curr index to the next non-digit position
            num = ''
            # print(curr)
            # print(data[curr])
            if data[curr] == '-':
                num = num + data[curr]
                curr += 1
            while(data[curr].isnumeric()):
                num = num + data[curr]
                curr += 1
            # print(num)
            return num
        
        
        if data[0] == 'n':
            return None
        
        stack = []
        root = TreeNode(int(getEle()))
        
        stack.append(root)
        node = root
        # initialize start node and recurrence stack
        
        while(curr < len(data)):
            s = getEle()
            # get the next action, s means "symbol"
            if s == 'l':
                ele = getEle()
                if ele == 'n':
                    continue
                else:
                    node.left = TreeNode(int(ele))
                    stack.append(node)
                    node = node.left
            if s == 'r':
                ele = getEle()
                if ele == 'n':
                    continue
                else:
                    node.right = TreeNode(int(ele))
                    stack.append(node)
                    node = node.right
            if s == 'b':
                node = stack.pop(-1)
        
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))