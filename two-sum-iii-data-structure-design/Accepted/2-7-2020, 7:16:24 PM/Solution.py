// https://leetcode.com/problems/two-sum-iii-data-structure-design

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.dict:
            self.dict[number] += 1
        else:
            self.dict[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for _ in self.dict:
            if _ == value/2 :
                if self.dict[_] > 1:
                    return True
            else:
                if (value-_) in self.dict:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)