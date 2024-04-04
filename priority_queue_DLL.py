''' Priority Queue using DLL()'''

class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next
    
class priorityQueue:
    def __init__(self):
        self.myqueue = None
        self.items_count = 0

    def push(self,data,priority):
        n = Node(data,priority)
        if self.is_empty() or self.myqueue.priority > priority:
            n.next = self.myqueue
            self.myqueue = n
        else:
            temp = self.myqueue
            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n   
        self.items_count +=1
    def is_empty(self):
        return self.myqueue == None

    def pop(self):
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        data = self.myqueue.item
        self.myqueue = self.myqueue.next
        self.items_count -=1
        return data
    def size(self):
        return self.items_count

# driver code
p = priorityQueue()
p.push('Rohit',3)
p.push('Amit',2)
p.push('sonim',6)
p.push('hari',9)
p.push('hari',11)
p.push('riti',7)
# order forms is amit rohit sonim riti nabina
print('Priority queue size is ', p.size())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print('Priority queue size is ', p.size())
            