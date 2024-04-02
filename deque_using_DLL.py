''' Deque Data Structure using Doubly Linked List'''

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self,deque=None):
        self.deque = deque
        self.item_count = 0
    def is_empty(self):
        return self.deque == None
    
    def insert_front(self,data):
        n = Node(None,data,self.deque)
        self.deque = n
        self.deque.prev = self.deque

        self.item_count +=1
    def insert_rear(self,data):
        temp = self.deque
        while temp.next != None:
            temp = temp.next
        n = Node(temp,data,None)
        if temp == None:
            self.start = n
        else:
            temp.next = n 
        self.item_count +=1
        
    
    def get_front(self):
        if not self.is_empty():
            return self.deque.item
        else:
            raise IndexError('No data in the Deque')
    def get_rear(self):
        if not self.is_empty():
            if self.deque.next == None:
                return self.deque.item
            else:
                temp = self.deque
                while temp.next != None:
                    temp = temp.next
                return temp.item
        else:
            raise  IndexError('No data in the deque')

    def delete_front(self):
        if not self.is_empty():
            data = None
            if self.deque.next == None:
                data = self.deque
                self.deque = None
            else:
                data = self.deque.item
                self.deque = self.deque.next
                self.item_count -=1
            return data
        else:
            raise  IndexError('No data in the deque')

    def delete_rear(self):
        if not self.is_empty():
            data = None
            if self.deque.next == None:
                data = self.deque
                self.deque = None
            else:
                temp = self.deque
                while temp.next.next != None:
                    temp = temp.next
                data = temp.next.item
                temp.next = None
                self.item_count -=1
            return data
        else:
            raise  IndexError('No data in the deque')

    def size(self):
        return self.item_count      
        
#driver code
d = Deque()
d.insert_front(10)
d.insert_rear(20)
d.insert_front(30)
d.insert_rear(40)
# data is: 30 10 20 40
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is ',d.size())
print()
print('delete deque front data is',d.delete_front())
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is ',d.size())
print()
print('delete deque rear data is',d.delete_rear())
print('Deque front data is ',d.get_front())
print('Deque rear data is ',d.get_rear())
print('Deque data count is ',d.size())


