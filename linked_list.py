class node :
    def __init__(self,value):
        self.info = value
        self.next = None

def insertat_last(start):# inserting the user input value
    last = start
    st = int(input("Enter the number you want to create :"))
    for i in range(st):
        value = int(input("Enter the node value :"))
        a  = node(value)
        last.next = a
        last=a
    
def travarse(start):#printing the linked list
    n= start
    while n!= None:
        print(n.info)
        n = n.next
def insertatbegining(start):
    nam = int(input("Enter value for the begining node :"))
    new = node(nam)# inserting the value into calling node class  
    new.next = start # inserting into the start using new's next
    start = new
    return start
def deleteatbegining(start):
    new = start
    start = start.next # changing the start next into start's next address
    del new
    return start #after deleting element return the whole linked list
def deletelastnode(start):
    temp = start
    while temp.next != None:
        prev = temp
        temp = temp.next
    del temp
    prev.next = None
    return start
def insertafterspecificitem(start,item):
    am = int(input('enter insert value: '))
    new = node(am)
    temp = start
    while temp.info != item:# loop will execute until item not found 
        temp = temp.next # temp is changed to temp's next node
    new.next = temp.next # new variable is change when item found and changes to temp's next node
    temp.next = new # this will attach to specific 
    return start
def deleteafterspecificitem(start,item):
    temp = start
    while temp != None and temp.info != item: # loop will work until temp is not none and item found in temp 
        prev = temp # prev stores the previous temp node
        temp = temp.next # temp is change to it's next
    if temp != None:
        prev.next = temp.next # prev's next is change to temp's next when temp is not None
    else:
        print("Item does not in the list ")
    del temp # deleting the item when item found in temp
    return start
def insertatposition(start,post):
    am = int(input('Enter the no you want to enter '))
    new = node(am)
    temp = start
    for i in range(1,post): # it will iterate whole node until position passed by the user
        temp = temp.next # change the temp to temp's next until poition-1 size
    new.next = temp.next # attach or say insert the new's next to temp.next . 
    temp.next = new # insert the new node to temp's next node
    return start
def deleteatposition(start,post):
    temp = start
    for i in range(1,post):# it will iterate whole node until position passed by the user
        prev = temp # prev stores the temp node 
        temp = temp.next # temp is change to its next node
    prev.next = temp.next # prev's next is change to temp's next node
    del temp # deleting the specific position node
    return start # changing whole node is passed / return
    

start = node(12)
insertat_last(start)
travarse(start)
start = insertatbegining(start) # changing the start (whole node ) after insert at begining
travarse(start) # printing the full node by calling travarse function
start = deleteatbegining(start)# changing the start after the deleting first node
print("After deleting the first node ")
travarse(start) 
start = deletelastnode(start)
print("After deleting the last node ")
travarse(start)
item = int(input("Choose any specific number "))
start = insertafterspecificitem(start,item)
travarse(start)
item = int(input('Enter the number you want to delete '))
start = deleteafterspecificitem(start,item)
print("After deleting node ")
travarse(start)
post = int(input('Enter the specific position '))
start = insertatposition(start,post)
travarse(start)
post = int(input('Enter the specific position you want to delete '))
start = deleteatposition(start,post)
print("After deleting position ")
travarse(start)

'''start.next = node(14)
start.next.next = node(18)

print(start.info)
print(start.next)
print(start.next.info)
print(start.next.next)
last = start
for i in range(5):
    value = input()
    a  = node(value)
    last.next = a
    last=a
n= start
while n!= None:
    print(n.info)
    n = n.next
'''
