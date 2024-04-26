class Stack:
    def __init__(self,arr):
        self.arr = arr
        self.top = 0
        
    def push(self,item):
        self.item =item 
        if self.top ==(len(self.arr)-1):
            print("Stack is full ")
            return self.top
        self.top += 1
        self.arr[self.top] = self.item
        return self.arr
    def pop(self):
        if self.top == -1:
            print('Stack is empty ')
            return self.top
        self.item = self.arr[self.top]
        self.top -= 1
        return self.item
l = []
ob = Stack(l)
print(ob.push(10))
print(ob.push(12))
print(ob.pop(10))
