// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        root = Node(1)
        seen[root.val] = root
        
        def printNeighbors(node: 'Node'):
            count = 0
            for neighbor in node.neighbors:
                count += 1
                print("neighbor " + str(count) + ": " + str(neighbor.val))
        
        def traverse(node: 'Node', copy: 'Node', seen: dict):
            # print(copy.val)
            # printNeighbors(copy)
            # print(seen)
            if node.neighbors is None:
                return
            for neighbor in node.neighbors:
                if neighbor.val not in seen:
                    temp = Node(neighbor.val)
                    seen[neighbor.val] = temp
                    copy.neighbors.append(temp)
                    traverse(neighbor, temp, seen)
                else:
                    temp = seen[neighbor.val]
                    copy.neighbors.append(temp)
                    
        traverse(node, root, seen)
        # printNeighbors(root)
        # printNeighbors(root.neighbors[0])
        return root
                    