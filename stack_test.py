class stack:
    def __init__(self):
        self.st = list()
        #self.item = i
        self.top = -1
        self.size= 9
    def push(self,item):
        self.item = item
        if self.top == self.size-1:
            print ('stack is full')
            return self.top
        self.top += 1
        self.st.append( self.item)
    def pop(self,i):
        self.item = i
        if self.top == -1:
            print('Stack is empty ')
            return self.top
        self.st.pop(self.item)
        self.top -= 1
    def display(self):
        print(self.st)
ob = stack()
ob.push(20)
ob.push(30)
ob.display()
ob.pop(0)
ob.display()
