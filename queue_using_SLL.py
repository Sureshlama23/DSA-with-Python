''' Queue Data Structure using Singly Linked List Concept'''

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class Queue:
    def __init__(self,myqueue=None):
        self.queue_count = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.queue_count +=1
    
    def dequeue(self):
        data = None
        if self.is_empty():
            raise IndexError('No data in the queue')
        elif self.front == self.rear:
            data = self.front
            self.front = None
            self.rear = None
        else:
            data = self.front
            self.front = self.front.next
        self.queue_count -= 1
        return data.item
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('No data in the queue')
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError('No data in the queue')
        else:
            return self.rear.item
    def size(self):
        return self.queue_count
        

#driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print('Queue get front value is',q.get_front())
print('Queue get rear value is ',q.get_rear())
print('Queue value count is',q.size())
print('Dequeue value is',q.dequeue())
print('Queue get front value is',q.get_front())
print('Queue get rear value is ',q.get_rear())
print('Queue value count is',q.size())

        