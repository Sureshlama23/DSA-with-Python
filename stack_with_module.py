import SLL_copy
''' Stack using import SLL() class making object'''

class stack:
    def __init__(self):
        self.top = SLL_copy.SLL()
        self.item_count = 0
    def is_empty(self):
        return self.top == None
    def push(self,data):
        self.item_count +=1
        self.top.insert_start(data)
    
    def pop(self):
        if not self.is_empty():
            self.item_count -=1
            data = self.top.start.item
            self.top.delete_first()
            return data
    
    def peek(self):
        if not self.is_empty():
            return self.top.start.item
    
    def size(self):
        return self.item_count

st1 = stack()
st1.push(10)
st1.push(20)
st1.push(30)
print('Top stack item is:- ',st1.peek())
print('stack size is:- ',st1.size())
print()
print('Stack remove item is: ',st1.pop())
print('Top stack item is:- ',st1.peek())
print('stack size is:- ',st1.size())
st1.is_empty()
