''' Stack DSA '''

class stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('stack is empty')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('stack is empty')
    
    def size(self):
        if not self.is_empty():
            return len(self.items)
        
mystack = stack()
mystack.push(3)
mystack.push(5)
mystack.push(10)
mystack.push(20)
print("This a top items",mystack.peek())
print('Remove element is',mystack.pop())
print("This a top items",mystack.peek())
print('Size of elements',mystack.size())