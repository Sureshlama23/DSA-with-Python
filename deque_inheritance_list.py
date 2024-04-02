''' Deque Data Structure using inheritance list'''

class Deque(list):
    def is_empty(self):
        return len(self) == 0
    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
        self.append(data)
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('No data in the Deque')
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('No data in the Deque')
    def delete_front(self):
        if not self.is_empty():
            data = self[0]
            self.pop(0)
            return data
        else:
            raise IndexError('No data in the Deque')
    def delete_rear(self):
        if not self.is_empty():
            data = self[-1]
            self.pop()
            return data
        else:
            raise IndexError('No data in the Deque')
    def size(self):
        return len(self)
    def clear(self):
        raise AttributeError("Deque has no 'clear()' attribute")
    def extend(self):
        raise AttributeError("Deque has no 'extend()' attribute")
    def sort(self):
        raise AttributeError("Deque has no 'sort()' attribute")
    def copy(self):
        raise AttributeError("Deque has no 'copy()' attribute")
    def remove(self):
        raise AttributeError("Deque has no 'remove()' attribute")
    def reverse(self):
        raise AttributeError("Deque has no 'reverse()' attribute")

#driver code
d = Deque()
# [50,10,20,30,40]
d.insert_front(10)
d.insert_rear(20)
d.insert_rear(30)
d.insert_rear(40)
d.insert_front(50)
d.reverse()
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