"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
then it should throw an error or return null.

max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
then it should throw an error or return null.

Each method should run in constant time.
"""

class stack:
    def __init__(self):
        self.st = []
        self.max_st = []
        self.len = 0

    def push(self, val):
        if self.len == 0:
            self.max_st.append(val)
        else:
            if self.max_st[-1] > val:
                self.max_st.append(self.max_st[-1])
            else:
                self.max_st.append(val)
        self.st.append(val)
        self.len += 1

    def max(self):
        if self.len == 0:
            return -1
        else:
            return self.max_st[-1]

    def pop(self):
        if self.len == 0:
            self.max_st.pop()
            return self.st.pop()
        else:
            self.max_st.pop()
            return self.st.pop()


st_obj = stack()
st_obj.push(1)
st_obj.push(9)
st_obj.push(4)
st_obj.push(1)
print(st_obj.max())
st_obj.pop()
st_obj.pop()
st_obj.pop()
print(st_obj.max())