class node:
    def __init__(self,v):
        self.prev = None
        self.info = v
        self.next = None
class DlinkedList:
    def __init__(self):
        self.start = None
    def insertatlast(self,v):
        n = node(v)
        if self.start == None:
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
            n.prev = temp
    def insertatbeg(self,v):
        n = node(v)
        temp = self.start
        while temp.next != None:
            temp = temp.next
        self.start.prev = n
        n.next = self.start
        self.start = n
    def travarse(self):
        temp = self.start
        while temp.next !=None:
            print(temp.info)
            temp= temp.next
        print(temp.info)
    def deletelastnode(self):
        temp = self.start
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp
    def deleteatbeg(self):
        temp = self.start
        self.start = self.start.next
        self.start.prev = None
        del temp
    def insertatspecificposition(self,p,v):
        n = node(v)
        temp = self.start
        for i in range(1,p):
            temp = temp.next
            #previ = temp
        n.next = temp.next
        previ = temp.next
        temp.next = n
        n.prev = temp
        previ.prev = n
    def insertafterspecificitem(self,item,v):
        n = node(v)
        temp = self.start
        while temp.info != item:
            temp = temp.next
        n.next = temp.next
        previ = temp.next
        n.prev = temp
        temp.next = n
        previ.prev = n
    def deleteatspecificitem(self,item):
        temp = self.start
        while temp.info != item:
            previ = temp
            temp = temp.next
        previ.next = temp.next
        previ.prev = temp.prev
        del temp
    def deleteatspecificpost(self,p):
        temp = self.start
        for i in range(1,p):
            previ = temp
            temp = temp.next
        previ.next = temp.next
        var = temp
        temp = temp.next
        del var
        
dl = DlinkedList()
dl.insertatlast(20)
dl.insertatlast(40)
dl.insertatlast(48)
print("After insert at last ")
dl.travarse()

dl.insertatbeg(10)
print("After insert at first ")
dl.travarse()
dl.deletelastnode()
print("After deleting last node ")
dl.travarse()
dl.deleteatbeg()
print("After deleting first node ")
dl.travarse()
dl.insertatspecificposition(1,49)
print("After inserting at specific position ")
dl.travarse()
dl.insertafterspecificitem(20,28)
print("After inserting after specific item ")
dl.travarse()
dl.deleteatspecificitem(28)
print("After deleting specific item ")
dl.travarse()
dl.deleteatspecificpost(2)
print("After deleting the specific node ")
dl.travarse()


