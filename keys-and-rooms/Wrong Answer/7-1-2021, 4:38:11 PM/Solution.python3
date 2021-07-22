// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        n = len(rooms)
        
        for i in range(1, len(rooms)):
            if i in keys:
                cur = set(rooms[i])
                keys.update(cur)
            else:
                return False
        
        return True
        
        
        
        