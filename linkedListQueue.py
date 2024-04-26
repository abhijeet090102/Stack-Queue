class node :
    def __init__(self,v):
        self.info = v
        self.next = None
class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def deletion(self):
        temp = self.front # temperary variable is pointing to front for deleting the element
        if self.front == None and self.rear == None:
# if queue is empty means front and rear is none than return None 
            print("Queue is empty ")
            return self.front
        else:
# else part run when queue is not empty then deleting the element from front of linked list 
            self.front = temp.next # this will point the front value to it's next node for deleting the element
            temp.next = None
            # linked list first's next part is now empty and now deleting the first node 
            del temp
            
    def insert (self,v):
        n = node(v) # new node will be created with calling node class 
        if self.rear  == None and self.front == None:
# if both queue's front and rear is empty then new node will attach to it 
            self.front = n
            self.rear = n
        else:
# if Queue is not empty then Queue's rear will point to new node and it's next is also point to new node
            self.rear.next = n
            self.rear = n
    def travarse(self):
        temp = self.front
        while temp.next!= None:
            print(temp.info)
            temp = temp.next
        print(temp.info)
        
lq = LQueue()
lq.insert(20)
lq.insert(40)
lq.insert(60)
print("After inserting at node in Queue ")
lq.travarse()
lq.deletion()
print("After deleting the node from Queue ")
lq.travarse()
