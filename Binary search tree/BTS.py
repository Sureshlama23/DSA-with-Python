'''
    This is preorder Binary Search Tree r means recursive
'''

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

class BTS:
    
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root == None
    
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if root.item > data:
            root.left = self.rinsert(root.left,data)
        elif root.item < data:
            root.right = self.rinsert(root.right,data)
        return root
            
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root == None or root.item == data:
            return root.item if root else None
        if root.item < data:
            return self.rsearch(root.right,data)
        else:
            return self.rsearch(root.left,data)
    
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
        
        
        
b = BTS()
print(b.is_empty())
b.insert(40)
b.insert(10)
b.insert(20)
b.insert(30)
print(b.is_empty())    
print(b.preorder())  
print(b.search(70))
print(b.inorder())
print(b.postorder())

            
            
        