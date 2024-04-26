class LinearQueue:
    def __init__(self):
        self.queue = list()
        self.front =-1
        self.rear =-1
    def Deletion(self,i):
        self.item = i
        if self.front == -1 and self.rear == -1:
            print('Queue is empty')
            return self.front
        self.queue.pop(self.item)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front +=1
        return self.item
    def Insert(self,i):
        self.item = i
        self.size = 9
        if self.rear == self.size:
            print('Queue is full ')
            return self.rear
        self.rear += 1
        self.queue.append(self.item)
        if self.front == -1:
            self.front = 0
    def display(self):
        print(self.queue)
        
ob = LinearQueue()
ob.Insert(20)
ob.Insert(40)
ob.display()
ob.Deletion(0)
ob.display()
