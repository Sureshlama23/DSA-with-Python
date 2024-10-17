class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None 
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        temp = self.start
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n 
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
        
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=', ')
            temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:    
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def remove_duplicate(self):
        if self.start is None:
            return None
        
        current = self.start
        seen_items = set()
        prev = None
        
        while current is not None:
            if current.item in seen_items:
                prev.next = current.next
            else:
                seen_items.add(current.item)
                prev = current
            current = current.next
        return self.start

# Driver Code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(20), 30)
mylist.insert_at_last(10)
mylist.insert_at_last(40)
mylist.insert_at_start(20)

# Print list before removing duplicates
print("Original List:")
mylist.print_list()
# Remove duplicates
mylist.remove_duplicate()

# Print list after removing duplicates
print("List after removing duplicates:")
mylist.print_list()
