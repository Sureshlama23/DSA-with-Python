# DOUBLY LINK LIST

# This node
class Node:

  def __init__(self,prev=None,item=None,next=None):
    self.prev = prev
    self.item = item 
    self.next = next
  
# DLL class
class DLL:
  def __init__(self,start=None):
    self.start = start
  def is_empty(self):
    return self.start == None
  def insert_start(self,data):
    n = Node(None,data,self.start)
    self.start = n
    self.start.prev = self.start
  def insert_last(self,data):
    # own code ----------------->>>>>>>>>>
    n = Node(None,data)
    if self.start is None:
      self.start = n
    elif self.start.next is None:
      self.start.next = n
      n.prev = self.start
    else:
      temp = self.start
      while temp.next is not None:
        temp = temp.next
      temp.next = n
      n.prev =temp

    # teacher code
    # temp = self.start
    # while temp.next != None:
    #   temp = temp.next
    # n = Node(temp,data,None)
    # if temp == None:
    #   self.start = n
    # else:
    #   temp.next = n 

  def search(self,data):
    temp = self.start
    while temp is not None:
      if temp.item == data:
        return temp
      temp = temp.next
    return None
  def insert_after(self,temp,data):
    # my code
    if temp is not None:
      n = Node(temp,data,temp.next)
      temp.next = n
  def delete_first(self):
    if self.is_empty():
      pass
    elif self.start.next is None:
      self.start = None
    else:
      self.start = self.start.next
      self.start.prev = None
  def delete_last(self):
    if self.is_empty():
      pass
    elif self.start.next is None:
      self.start = None
    else:
      #my code
      # temp = self.start
      # while temp.next.next is not None:
      #   temp = temp.next
      # temp.next = None
      #teacher code
      temp = self.start
      while temp.next != None:
        temp = temp.next
      temp.prev.next = None
      
  def delete_item(self,data):
    # my code
   if self.is_empty():
      pass
   elif self.start.next is None:
     if self.start.item == data:
       self.start = None
   else:
     if self.start.item == data:
       self.start = self.start.next
       self.start.prev = None
     else:
       temp = self.start
       while temp.next is not None:
         if temp.next.item == data:
           temp.next = temp.next.next
           break
         temp = temp.next
          
  def print_list(self):
    temp = self.start
    while temp is not None:
      print(temp.item,end=' ')
      temp = temp.next
  def __iter__(self):
    return DLLIterator(self.start)

class DLLIterator:
  def __init__(self,start):
    self.current = start
  def __iter__(self):
    return self
  def __next__(self):
    if not self.current:
      raise StopIteration
    data = self.current.item
    self.current = self.current.next
    return data

#Driver code
mylist = DLL()
mylist.insert_start(10)
mylist.insert_last(15)
mylist.insert_start(20)
mylist.insert_last(5)
mylist.print_list()
mylist.insert_after(mylist.search(20),30)
print()
mylist.print_list()
print()
mylist.delete_item(20)
for x in mylist:
  print(x,end=' ')
