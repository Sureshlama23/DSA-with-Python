""" Stack with Linked list"""

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    

class stack:
    def __init__(self,top=None):
        self.top = top
        self.item_count = 0
    
    def is_empty(self):
        return self.top == None    
    
    def push(self,data):
        n = Node(data,self.top)
        self.item_count += 1
        self.top = n
    
    def peek(self):
        if not self.is_empty():
          return self.top.item
        else:
            raise self.is_empty()
    
    def pop(self):
        if not self.is_empty():
            data = self.top.item
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack is empty')
           
    def size(self):
        return self.item_count
        

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Top value is= ',s1.peek())
print('stack size is',s1.size())
print()
print('Remove value is=',s1.pop())
print('Top value is= ',s1.peek())
print('stack size is',s1.size())