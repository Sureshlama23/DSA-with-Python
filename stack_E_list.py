''' Stack extending with list'''


    
class stack(list):
    def is_empty(self):
          return len(self)==0

    def push(self,data):
        self.append(data)
    
    def peek(self):
        if not self.is_empty():
          return self[-1]
        else:
            raise IndexError('Stack is empty')
    
    def pop(self):
        if not self.is_empty():
          return super().pop()
        else:
            raise IndexError('Stack is empty')
    def insert(self,data):
         if self is self.insert(data):
              raise IndexError('No permission')

    def size(self):
         return len(self)

    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in Stack")

s1 = stack()
s1.push(10)
s1.push(19)
s1.push(5)
print('Top elements is',s1.peek())
print('Remove element is',s1.pop())
print('Stack size is',s1.size)
print('Top elements is',s1.peek())
s1.insert(1,20)