"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""
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
        new_min = x #0
        curr_min = self.getMin() #1
        if new_min < curr_min or curr_min is None:
            self.minstk.append(new_min)
        else:
            self.minstk.append(curr_min)
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
        self.minstk.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stk[len(self.stk)-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minstk) == 0:
            return None
        else:
            return self.minstk[len(self.minstk)-1]