''' Deque Data Structure using a List'''

class Deque:
    def __init__(self):
        self.deque = []
    def is_empty(self):
        return len(self.deque) == 0
    
    def insert_front(self,data):
        self.deque.insert(0,data)
    def insert_rear(self,data):
        self.deque.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            data = self.deque[0]
            self.deque.pop(0)
            return data
        else:
            raise IndexError('No data in the Deque')
    def delete_rear(self):
        if not self.is_empty():
            data = self.deque[-1]
            self.deque.pop()
            return data
        else:
            raise IndexError('No data in the Deque')
    
    def get_front(self):
        if not self.is_empty():
            return self.deque[0]
        else:
            raise IndexError('No data in the Deque')
    def get_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        else:
            raise IndexError('No data in the Deque')

    def size(self):
        return len(self.deque)
#driver code
d = Deque()
# [50,10,20,30,40]
d.insert_front(10)
d.insert_rear(20)
d.insert_rear(30)
d.insert_rear(40)
d.insert_front(50)
print('Deque front data is',d.get_front())
print('Deque rear data is',d.get_rear())
print('Deque data count is',d.size())
print('Deleted front data is',d.delete_front())
print()
print('Deque front data is',d.get_front())
print('Deque rear data is',d.get_rear())
print('Deque data count is',d.size())
print()
print('Deleted rear data is',d.delete_rear())
print('Deque front data is',d.get_front())
print('Deque rear data is',d.get_rear())
print('Deque data count is',d.size())

#  Tested successfull