class node:
    def __init__(self,v):
        self.info = v
        self.next = None
class LStack:
    def __init__(self):
        self.start = None
        self.top = None
    def push(self,v):
        n = node(v)
        if self.start == None :
            self.start = n
            self.top = n
        else:
            self.top.next = n
            self.top = n

    def pop(self):
        if self.start == None :
            print("Stack is empty ")
            return
        else:
            if self.start == self.top :
                temp = self.start
                self.start = None
                self.top = None
            else:
                prev = self.start
                while prev.next!= self.top :
                    prev = prev.next
                var = self.top
                self.top = prev
                self.top.next = None
                del var
    def display(self,n):
        self.travarse(n)
        
    def travarse(self,n):
        if n.next != None:
##            print(n.info)
            self.display(n.next)
            
        if n.next != None :
            print(n.info)
        
st = LStack()
st.push(20)
st.push(40)
st.push(80)
st.push(42)
st.push(82)
st.pop()
st.display(st.start)
