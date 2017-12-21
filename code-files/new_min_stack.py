__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # new_min = x
        # curr_min = self.getMin()
        # if new_min < curr_min or curr_min is None:
        #     self.minstk.append(new_min)
        # else:
        #     self.minstk.append(curr_min)
        # self.stk.append(x)
        if len(self.stk) == 0 or self.minval > x:
            self.minval = x
        self.stk.append(x)
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stk) == 0:
            return None
        if len(self.minstk) == 0:
            return None
        val = self.stk.pop()
        if val == self.getMin():
            temp_min = self.top()
            for i in range(0, len(self.stk)-2):
                if temp_min > self.stk[i]:
                    temp_min = self.stk[i]
            self.minval = temp_min
        #self.minstk.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stk[len(self.stk)-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            return None
        else:
            return self.minval
