''' Queue with module'''

from SLL_copy import *

class Queue:
    def __init__(self):
        self.myqueue = SLL()
        self.queue_count = 0
    
    def is_empty(self):
        return self.myqueue == None
    def enqueue(self,data):
        self.queue_count +=1
        self.myqueue.insert_start(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.queue_count -=1
            temp = self.myqueue.start
            while temp.next.next != None:
                temp = temp.next
            data = temp.next.item
            temp.next = None
            return data
        
    def get_front(self):
        if not self.is_empty():
            temp = self.myqueue.start
            while temp.next != None:
                temp = temp.next
            return temp.item
        
    def get_rear(self):
        if not self.is_empty():
            return self.myqueue.start.item
    
    def size(self):
        return self.queue_count
    
#Driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print('Queue get front value is ',q.get_front())
print('Queue get real value is ',q.get_rear())
print('Queue value count is ',q.size())
print('Dequeue value is ',q.dequeue())
print()
print('Queue get front value is ',q.get_front())
print('Queue get real value is ',q.get_rear())
print('Queue value count is ',q.size())