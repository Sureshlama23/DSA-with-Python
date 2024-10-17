''' Priority queue using list'''

class priorityQueue:
    def __init__(self):
        self.items = []
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<= priority:
            index +=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items) == None
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is empty')
        else:
            return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    
# driver code
p = priorityQueue()
p.push('sabin',2)
p.push('rakesh',5)
p.push('sonim',1)
p.push('ajay',3)
p.push('nabin',6)
print(p.items)
print('Queue items count is ',p.size())
print()
# while not p.is_empty():
#     print(p.pop())
print('Queue items count is ',p.size())
