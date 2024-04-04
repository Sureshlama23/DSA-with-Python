''' Deque Data Structure with DLL() concept'''

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.front == None:
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count +=1
    def insert_rear(self,data):
        n = Node(data,self.rear,None)
        if self.front == None:
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count +=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError('No data in the Deque')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('No data in the Deque')

    def delete_front(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                data = self.front.item
                self.front = self.front.next
                self.front.prev = None
                self.item_count -=1
                return data
        else:
            raise IndexError('No data in the Deque')
    def delete_rear(self):
        if not self.is_empty():
            data = None
            if self.front == self.rear:
                data = self.front.item
                self.front = None
                self.rear = None
            else:
                data = self.rear.item
                self.rear = self.rear.prev
                self.rear.next = None
            self.item_count -=1
            return data
        else:
            raise IndexError('No data in the Deque')

    def size(self):
        return self.item_count

#driver code
d = Deque()
d.insert_rear(30)
d.insert_front(20)
d.insert_rear(40)
d.insert_front(10)
# 10 20 30 40 
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is',d.size())
print()
print('Deque front deleted data is ',d.delete_front())
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is',d.size())
print()
print('Deque rear deleted data is ',d.delete_rear())
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is',d.size())
print()
print('Deque rear deleted data is ',d.delete_rear())
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is',d.size())

