'''Queue Data Structure using list.'''

class Queue:
    def __init__(self):
        self.myqueue = []
        self.queue_count = 0
    def is_empty(self):
        return self.myqueue == None
    def enqueue(self,data):
        self.queue_count +=1
        self.myqueue.insert(0,data)
    def dequeue(self):
        if not self.is_empty():
            self.queue_count -=1
            data = self.myqueue[-1]
            self.myqueue.pop()
            return data
        else:
            raise IndexError('No value for dequeue')
    def get_front(self):
        if not self.is_empty():
            return self.myqueue[-1]
        else:
            raise IndexError('No value get in front')
    def get_rear(self):
        if not self.is_empty():
            return self.myqueue[0]
        else:
            raise IndexError('No value get in rear')
    def size(self):
        print(self.myqueue)
        return self.queue_count

#driver code   
q = Queue()
q.enqueue(10)
q.enqueue(40)
q.enqueue(30)
q.enqueue(20)
print('Get Front value is',q.get_front())
print('Get Rear value is',q.get_rear())
print('Queue count is',q.size())
print('Dequeue value is',q.dequeue())
print()
print('Get Front value is',q.get_front())
print('Get Rear value is',q.get_rear())
print('Queue count is',q.size())


        
    