// https://leetcode.com/problems/robot-room-cleaner

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.cleaned = set()
        self.curr = (0, 0)
        self.direction = 0
        # starting pos: (0, 0), facing up
        # up: 0, left: 1, down: 2, right: 3
        
        # def turnRobot(robot, end_dir):
        #     l = (end_dir - self.direction) % 4
        #     for _ in range():
        #         robot.turnLeft()
        
        def posTowardDirection():
            if self.direction == 0:
                return (self.curr[0], self.curr[1] + 1)
            elif self.direction == 1:
                return (self.curr[0] - 1, self.curr[1])
            elif self.direction == 2:
                return (self.curr[0], self.curr[1] - 1)
            else:
                return (self.curr[0] + 1, self.curr[1])
        
        def track(robot):
            # print(self.direction)
            # print(self.curr)
            # print()
            robot.clean()
            self.cleaned.add(self.curr)
            
            robot.turnLeft()
            self.direction = (self.direction + 1) % 4
            for _ in range(3):
                row, col = posTowardDirection()
                if (row, col) not in self.cleaned and robot.move():
                    self.curr = (row, col)
                    track(robot)
                    robot.turnLeft()
                    self.direction = (self.direction + 1) % 4
                else:
                    robot.turnRight()
                    self.direction = (self.direction - 1) % 4
            
            self.curr = posTowardDirection()
            robot.move()
            return
        
        track(robot)
        
                
            
        
        
        