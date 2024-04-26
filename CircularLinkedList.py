class node:
    def __init__(self,v):
        self.info = v
        self.next = None
        
class circularlinked :
    def __init__(self):
        self.start = None
    def insertatlast(self,v):
        n = node(v)
        if self.start == None:
            self.start = n
            n.next = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = n
            n.next = self.start
    def travarse(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.info)
            temp = temp.next
        print(temp.info)
    def insertatbeg(self,v):
        n = node(v)
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        n.next = self.start
        self.start=n
        temp.next = self.start
        #n.next = self.start
        #self.start = n
    def deleteLastNode(self):
        temp = self.start
        while temp.next != self.start:
            prev = temp
            temp = temp.next
        prev.next = self.start
        del temp
    def deletefirstNode(self):
        temp = self.start
        if temp.next != self.start:
            temp = temp.next
        var = self.start
        self.start = self.start.next
        temp.next = self.start
        del var
    def insertafterspecificpost(self,v,p):
        n = node(v)
        temp = self.start
        for i in range(1,p):
            temp = temp.next
        n.next = temp.next
        temp.next = n
    def insertafterspecificitem(self,v,item):
        n = node(v)
        temp = self.start
        while temp.info != item:
            temp = temp.next
        n.next = temp.next
        temp.next = n
    def deleteAtspecificPost(self,post):
        temp = self.start
        for i in range(1,post):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp
    def deleteAtSpecificItem(self,item):
        temp = self.start
        while temp.next != self.start and temp.info != item:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp
        
am = circularlinked()
am.insertatlast(20)
am.insertatlast(40)
am.insertatlast(30)
print("After inserting at last node ")
am.travarse()
am.insertatbeg(10)
print("After insert at begining node ")
am.travarse()
am.deleteLastNode()
print("After deleting last node ")
am.travarse()
am.deletefirstNode()
print("After deleting first node ")
am.travarse()
am.insertatlast(1)
print("After insert at last ")
am.travarse()
am.insertafterspecificpost(28,1)
print("After insert after specific position ")
am.travarse()
am.insertafterspecificitem(24,28)
print("After insert at specific item ")
am.travarse()
am.deleteAtspecificPost(2)
print("After deleting at specific position ")
am.travarse()
am.deleteAtSpecificItem(28)
print("After deleting at specific item ")
am.travarse()
