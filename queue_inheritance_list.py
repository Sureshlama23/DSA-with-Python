''' Queue using Inheritance List'''

class Queue(list):

    def is_empty(self):
        return len(self) == 0
    def enqueue(self,data):
        self.insert(0,data)
    def dequeue(self):
        if not self.is_empty():
            data = self[-1]
            self.pop()
            return data
        else:
            raise IndexError('No in queue for dequeue')
    def get_front(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('No in queue for dequeue')
    
    def get_rear(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('No in queue for dequeue')
    def size(self):
        return len(self)
    
    def extend(self):
        raise AttributeError("Queue has no 'extend()' attribute")
    def copy(self):
        raise AttributeError("Queue has no 'copy()' attribute")
    def append(self,data):
        raise AttributeError("Queue has no 'append()' attribute")
    def clear(self):
        raise AttributeError("Queue has no 'clear()' attribute")
# Driver code
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
