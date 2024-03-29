'''Stack using inheritance SLL() '''
import SLL_copy

class stack(SLL_copy.SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.item_count += 1
        self.insert_start(data)

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Stack is empty')
    
    def pop(self):
        if not self.is_empty():    
            data = self.start.item
            self.item_count -= 1
            self.delete_first()
            return data
        else:
            raise IndexError('Stack is empty')
    def size(self):
        return self.item_count
    def delete_last(self):
        raise AttributeError("Stack has no 'delete_last()' attribute")
    def delete_item(self,temp,data):
        raise AttributeError("Stack has no 'delete_item()' attribute")
# driver code
# case 1
# s1 = stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print('Top value is: ',s1.peek())
# print('Stack size is:',s1.size())
# print()
# print('Remove item is: ',s1.pop())
# print('Top value is: ',s1.peek())
# print('Stack size is:',s1.size())

#case 2
s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Top value is: ',s1.peek())
print('Stack size is:',s1.size())
print()
print('Remove item is: ',s1.pop())
print('Top value is: ',s1.peek())
print('Stack size is:',s1.size())
# s1.delete_last()

# s1.delete_item(s1.search(10),20)
