// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        oldColor = image[sr][sc]
        
        if newColor == oldColor:
            return image
        
        def fill(r: int, c: int):
            image[r][c] = newColor
            if r > 0 and image[r-1][c] == oldColor:
                fill(r-1, c)
            if r < (m-1) and image[r+1][c] == oldColor:
                fill(r+1, c)
            if c > 0 and image[r][c-1] == oldColor:
                fill(r, c-1)
            if c < (n-1) and image[r][c+1] == oldColor:
                fill(r, c+1)
        
        fill(sr, sc)
        
        return image