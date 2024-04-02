''' Deque Data Structure using inheritance DLL'''
from DLL import DLL

class Deque(DLL):
    item_count = 0
    def is_empty(self):
        return super().is_empty()
    def insert_front(self, data):
        self.item_count +=1
        return self.insert_start(data)
    def insert_rear(self, data):
        self.item_count +=1
        self.insert_last(data)
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('No data in the Deque')
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError('No data in the Deque')
        
    def delete_first(self):
        if not self.is_empty():
            self.item_count -=1
            super().delete_first()
        else:
            raise IndexError('No data in the Deque')
    def delete_last(self):
        if not self.is_empty():
            self.item_count -=1
            super().delete_last()
        else:
            raise IndexError('No data in the Deque')

    def size(self):
        return self.item_count
    def delete_item(self, data):
        raise AttributeError(" Deque has no 'delete_item()' attribute")
    def insert_after(self, temp, data):
        raise AttributeError ("Deque has no 'insert_after()' attribute")

# driver code
d = Deque()
print('above result of DLL() class ')
print()
print()
d.insert_rear(30)
d.insert_front(20)
d.insert_rear(40)
d.insert_front(10)
# 10 20 30 40 
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is', d.size())
print()
d.delete_first() # remove 10
#left 20 30 40
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is', d.size())
print()
d.delete_last() # remove 40
#left 20 30
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is', d.size())

    