class stack:
    def __init__(self,s):
        self.st = []
        self.top = -1
        self.size = s
    def push (self,v):
        self.item = v
        if self.top == self.size -1:
            print('Stack is full ')
            return self.top
        self.top += 1
        self.st.insert(0,self.item)
    def pop (self):
        # self.index=0
        if self.top == -1 :
            print("Stack is empty ")
            return self.top
        self.st.pop()
        self.top -= 1
    def display(self):
        print(self.st)
st = stack(3)
# st.pop()
st.push(60)
st.push(40)
# st.pop()
st.push(20)
st.push(58)
st.push(42)
st.display()