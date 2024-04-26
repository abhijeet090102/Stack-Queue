class node :
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
            n.next = self.start
            n.prev = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = n
            n.prev = temp
            #temp.prev = n
            n.next = self.start
            self.start.prev = n
    def travarse(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.info)
            temp = temp.next
        print(temp.info)
    def insertatbeg(self,v):
        n = node(v)
        temp = self.start.prev
        temp.next = n
        n.next = self.start
        n.prev = temp
        self.start.prev = n
        self.start = n
    def deletelastnode(self):
        temp = self.start.prev
        previ = temp.prev
        previ.next = self.start
        self.start.prev = previ
        del temp

    def deleteatbeg(self):
        temp = self.start.next
        var = self.start
        temp.prev = self.start.prev
        last = temp.prev
        self.start = temp
        last.next = self.start
        del var
    def insertatspecificposition(self,p,v):
        n = node(v)
        temp = self.start
        for i in range(1,p):
            previ = temp
            temp = temp.next
        n.next = temp.next
        previ = temp.next
        temp.next = n
        n.prev = temp
        previ.prev = n
    def insertafterspecificitem(self,item,v):
        n = node(v)
        temp = self.start
        while temp.info != item:
            previ = temp
            temp = temp.next
        n.next = temp.next
        previ = temp.next
        temp.next = n
        n.prev = temp
        previ.prev = n
    def deleteatspecificpost(self,p):
        temp = self.start
        for i in range(1,p):
            previ = temp
            temp = temp.next
        previ.next = temp.next
        var = temp
        temp = temp.next
        temp.prev = previ
        del var
    def deleteatspecificitem(self,item):
        temp = self.start
        while temp.info != item :
            previ = temp
            temp = temp.next
        previ.next = temp.next
        var = temp
        temp = temp.next
        temp.prev = previ
        del var
dl = DlinkedList()
dl.insertatlast(40)
dl.insertatlast(20)
dl.insertatlast(39)
dl.travarse()
dl.insertatbeg(10)
print("After inserting at begining ")
dl.travarse()
dl.deletelastnode()
print("After deleting last node ")
dl.travarse()
dl.deleteatbeg()
print("After deleting first node ")
dl.travarse()
dl.insertatspecificposition(1,50)
print("After inserting at specific position ")
dl.travarse()
dl.insertafterspecificitem(20,200)
print("After inserting after specific item ")
dl.travarse()
dl.deleteatspecificpost(3)
print("After deleting the specific post ")
dl.travarse()

dl.deleteatspecificitem(20)
print("After deleting specific item ")
dl.travarse()
