class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curr_min = self.getMin() #1
        if curr_min is None or x < curr_min :
            self.minstk.append(x)
        else:
            self.minstk.append(curr_min)
        self.stk.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stk.pop()
        self.minstk.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minstk) == 0:
            return None
        else:
            return self.minstk[-1] #0