class node:
    def __init__(self,v):
        self.info = v
        self.next = None
class singleLinkedlist:
    def __init__(self):
        self.start = None
    def insertatlast(self,v):
        n = node(v)
        if self.start == None:
            self.start = n # checking if self.start is none then start will refer to new node
        else:
            temp = self.start # storing start node into temp variable
            while temp.next != None: # checking if temp's next node is not none then temp will refer to it's next node
                temp = temp.next
            temp.next = n # if temp is not none then it will insert new node to temp's next node
    def travarse(self):
        temp = self.start
        while temp != None:
            print(temp.info)
            temp = temp.next
    def insertatbeg(self,v):
        n = node(v)
        n.next = self.start
        self.start = n

    def deleteatbeg(self):
        temp = self.start
        self.start = self.start.next
        del temp

    def insertafterspecificitem(self,item):
        am = int(input("Enter item :"))
        n = node(am)
        temp = self.start
        while temp.info != item:
            temp = temp.next
        n.next = temp.next
        temp.next = n
        
    def deletespecificitem(self,item):
        temp = self.start
        while temp != None and temp.info != item:
            prev = temp
            temp = temp.next
        if temp != None:
            if self.start.info == item:
                self.start = self.start.next
            else:
                prev.next = temp.next
                del temp
        else:
            print("Item does not in the linked list ")
    def inseratspecificposition(self,post):
        am = int(input("Enter the item: "))
        new = node(am)
        temp = self.start
        for i in range(1,post):
            temp = temp.next
        new.next = temp.next
        temp.next = new
    def deleteatposition(self,post):
        temp = self.start
        for i in range(1,post):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp

        
sl = singleLinkedlist()
sl.insertatlast(20)
sl.insertatlast(30)
print("After entering the new node at last ")
sl.travarse()
sl.insertatbeg(40)
print("After entering the new node at begining ")
sl.travarse()
sl.deleteatbeg()
print("After deleting the new node at begining ")
sl.travarse()
st = int(input("Enter the specific item :"))
sl.insertafterspecificitem(st)
print("After entering the new node at specific position ")
sl.travarse()
am = int(input("Enter the item you want to delete :"))
sl.deletespecificitem(am)
print("After deleting the specific node ")
sl.travarse()
a = int(input("Enter the position you want to enter "))
sl.inseratspecificposition(a)#insetatspecificposition
print("After entering the new node at specific position ")
sl.travarse()
m = int(input("Enter the specific position you want to delete "))
sl.deleteatposition(m)
print("After deleting the specific position ")
sl.travarse()

