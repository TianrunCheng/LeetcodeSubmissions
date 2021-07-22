// https://leetcode.com/problems/the-skyline-problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        
        def merge(leftSky: list, rightSky: list) -> list:
            highSky = [[0, 0]]
            ll = len(leftSky)
            rl = len(rightSky)
            leftHeight = [0] * (ll + rl + 1)
            rightHeight = [0] * (ll + rl + 1)
            height = [0] * (ll + rl + 1)
            tempX = [0] * (ll + rl + 1)
            lp = 0
            r = 0
            for i in range(1, ll + rl + 1):
                if lp < ll and r < rl:
                    if leftSky[lp][0] == rightSky[r][0]:
                        tempX[i] = leftSky[lp][0]
                        height[i] = max(leftSky[lp][1], rightSky[r][1])
                        leftHeight[i] = leftSky[lp][1]
                        rightHeight[i] = rightSky[r][1]
                        lp += 1
                        r += 1
                        i += 1
                    elif leftSky[lp][0] < rightSky[r][0]:
                        tempX[i] = leftSky[lp][0]
                        leftHeight[i] = leftSky[lp][1]
                        rightHeight[i] = rightHeight[i - 1]
                        height[i] = max(leftHeight[i], rightHeight[i])
                        lp += 1
                        i += 1
                    else:
                        tempX[i] = rightSky[r][0]
                        rightHeight[i] = rightSky[r][1]
                        leftHeight[i] = leftHeight[i - 1]
                        height[i] = max(leftHeight[i], rightHeight[i])
                        r += 1
                        i += 1
                elif lp == ll and i < (ll + rl):
                    tempX[i] = rightSky[r][0]
                    rightHeight[i] = rightSky[r][1]
                    leftHeight[i] = leftHeight[i - 1]
                    height[i] = max(leftHeight[i], rightHeight[i])
                    r += 1
                    i += 1
                elif r == rl and i < (ll + rl):
                    tempX[i] = leftSky[lp][0]
                    leftHeight[i] = leftSky[lp][1]
                    rightHeight[i] = rightHeight[i - 1]
                    height[i] = max(leftHeight[i], rightHeight[i])
                    lp += 1
                    i += 1
                else:
                    break

            for i in range(1, ll + rl + 1):
                if height[i] != height[i - 1]:
                    highSky.append([tempX[i], height[i]])
                i += 1
            highSky.pop(0)
            return highSky


        n = len(buildings)
        skyLines = [[[0, 0], [0, 0]]]
        for i in range(0, n):
            skyLines.append([[buildings[i][0], buildings[i][2]], [buildings[i][1], 0]])
        skyLines.pop(0)

        i = 0
        while len(skyLines) > 1:
            i = 0
            while i <= len(skyLines) - 2:
                skyLines[i] = merge(skyLines[i], skyLines[i + 1])
                skyLines.pop(i + 1)
                i += 1

        if len(skyLines) > 0:
            return skyLines[0]
        else:
            return []
