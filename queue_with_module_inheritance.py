''' Queue using Inheritance Singly Linked List'''
from SLL_copy import *

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.queue_count=0
    def is_empty(self):
        return super().is_empty()
    def enqueue(self,data):
        self.queue_count +=1
        self.insert_start(data)
    def dequeue(self):
        if not self.is_empty():
            self.queue_count -=1
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            data = temp.next.item
            temp.next = None
            return data
        else:
            raise IndexError('No in queue for dequeue')
    def get_front(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError('No in queue for dequeue')
    
    def get_rear(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('No in queue for dequeue')
    def size(self):
        return self.queue_count
    
    def delete_last(self):
        raise AttributeError("Queue has no 'delete_last()' attribute")
    def insert_last(self,data):
        raise AttributeError("Queue has no 'insert_last()' attribute")
    def insert_after(self, temp, data):
        raise AttributeError("Queue has no 'insert_after()' attribute")
    def delete_item(self, data):
        raise AttributeError("Queue has no 'delete_item()' attribute")

        
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
print()
print('Queue get front value is',q.get_front())
print('Queue get rear value is ',q.get_rear())
print('Queue value count is',q.size())
