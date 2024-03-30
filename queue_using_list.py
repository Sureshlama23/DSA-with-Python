''' Queue Data Structure using Singly Linked List'''

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class Queue:
    def __init__(self,myqueue=None):
        self.myqueue = myqueue
        self.queue_count = 0

    def is_empty(self):
        return self.myqueue == None
    
    def enqueue(self,data):
        self.queue_count +=1
        n = Node(data,self.myqueue)
        self.myqueue = n
    
    def dequeue(self):
        if not self.is_empty():
            self.queue_count -=1
            temp = self.myqueue
            while temp.next.next != None:
                temp = temp.next
            data = temp.next.item
            temp.next = None
            return data
    
    def get_front(self):
        if not self.is_empty():
            temp = self.myqueue
            while temp.next is not None:
                temp = temp.next
            return temp.item
    def get_rear(self):
        if not self.is_empty():
            return self.myqueue.item
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

        