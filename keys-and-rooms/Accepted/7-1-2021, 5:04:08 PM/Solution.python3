// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        for k in rooms[0]:
            stack.append(k)
            
        keys = set(rooms[0])
        keys.add(0)
        n = len(rooms)
        
        while(len(stack) > 0):
            key = stack.pop()
            for k in rooms[key]:
                if k not in keys:
                    stack.append(k)
                    keys.add(k)
        
        
            
        return len(keys) == (n)
        
        