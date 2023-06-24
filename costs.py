"""
creating the classes:
"""

import numbers


class UnitCost:
    
    def __init__(self, cost, range_):

        if not(0 <= cost) or not(isinstance(cost, numbers.Number)):
            raise ValueError("invalid input the cost should be a positive number")

        self.cost = cost

        # 31 to 40 is blonged to Blocks
        if not(range_ in range(31, 41)):
            raise ValueError("Invalid index!!")
        
        self.index = range_

    def get_cost(self):

        return (self.cost, self.index)
    


class FloorCost:

    def __init__(self, cost, range_):

        if not(0 <= cost) or not(isinstance(cost, numbers.Number)):
            raise ValueError("invalid input the cost should be a positive number")

        self.cost = cost

        # 21 to 30 is blonged to Blocks
        if not(range_ in range(21, 31)):
            raise ValueError("Invalid index!!")
        
        self.index = range_

    def get_cost(self):

        return (self.cost, self.index)
    

    

class BlockCost:
    
    def __init__(self, cost, range_):

        if not(0 <= cost) or not(isinstance(cost, numbers.Number)):
            raise ValueError("invalid input the cost should be a positive number")
        
        self.cost = cost

        # 11 to 20 is blonged to Blocks
        if not(range_ in range(11, 21)):
            raise ValueError("invalid index!!")
        
        self.index = range_

    
    def get_cost(self):
        
        return (self.cost, self.index)
    
        

class TownCost:

    def __init__(self, cost, range_):

        # 1 to 10 is assigned for Town

        if not(0 <= cost) or not(isinstance(cost, numbers.Number)):
            raise ValueError("invalid input the cost should be a positive number")

        self.cost = cost

        if not(range_ in range(1, 11)):
            raise ValueError("Invalid index!!")
        
        self.index = range_

    def get_cost(self):

        return (self.cost, self.index)


