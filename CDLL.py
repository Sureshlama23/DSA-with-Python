''' Circle Doubly Linked List'''

class Node:
  def __init__(self,prev=None,item=None,next=None):
    self.prev = prev
    self.item = item
    self.next = next
  
class CDLL:
  def __init__(self,start=None):
    self.start = start
  def is_empty(self):
    return self.start == None
  
  def insert_at_start(self,data):
    n = Node(None,data,None)
    if self.is_empty():
      n.next = n
      n.prev = n
      self.start = n
    if self.start.next == self.start:
      n.next = self.start
      n.prev = self.start
      self.start = n
    else:
      n.next = self.start
      n.prev = self.start.prev
      self.start.prev.next = n
      self.start.next.prev = n
      self.start = n
  
  def insert_at_last(self,data):
    n = Node(None,data,None)
    if self.is_empty():
      n.next = n 
      n.prev = n
      self.start = n
    if self.start == self.start.next:
      n.next = self.start
      n.prev = self.start
      self.start.next = n
      self.start.prev = n
    else:
      n.next = self.start
      n.prev = self.start.prev
      self.start.prev.next = n
      self.start.prev = n
  
  def search(self,data):
    if self.is_empty():
      return None
    if self.start.next == self.start:
      if self.start.item == data:
        return self.start
    else:
      temp = self.start
      while temp != self.start.prev:
        if temp.item == data:
          return temp
        temp = temp.next
      if temp.item == data:
        return temp
      return None
        
  def insert_after(self,temp,data):
    if temp != None:
      n = Node(temp,data,temp.next)
      temp.next = n
      temp.next.next.prev = n

  def delete_first(self):
    if not self.is_empty():
      if self.start.next == self.start:
        self.start = None
      else:
        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next
  def delete_last(self):
    if not self.is_empty():
      if self.start.next == self.start:
        self.start = None
      else:
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev
  def delete_item(self,data):
    if not self.is_empty():
        temp = self.start
        if temp.item == data:
          self.delete_first()
        else:
          temp = temp.next
          while temp != self.start:
            if temp.item == data:
              temp.prev.next = temp.next
              temp.next.prev = temp.prev
              break
            if temp == self.start:
              if self.start.prev.item == data:
                self.delete_last()
                break       
            temp = temp.next
  def print_list(self):
    if not self.is_empty():
      temp = self.start
      while temp != self.start.prev:
        print(temp.item,end=' ')
        temp = temp.next
      print(temp.item)
  def __iter__(self):
    return CDLLIterator(self.start)

class CDLLIterator:
  def __init__(self,start):
    self.current = start
    self.start = start
    self.check = False
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current == None:
      raise StopIteration
    if self.current == self.start and self.check == True:
      raise StopIteration
    else:
      self.check = True
    data = self.current.item
    self.current = self.current.next
    return data
  

# driver code
cdll = CDLL()
cdll.insert_at_start(20)
cdll.insert_at_last(10)
cdll.insert_after(cdll.search(20),4)
cdll.print_list()
print()
cdll.delete_item(20)
cdll.print_list()
