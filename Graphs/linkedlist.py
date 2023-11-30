class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record
# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(5) ]
for index in range(4):
    myList[index].pointer = index + 1
#next index
myList[4].pointer = -1
start = -1
nextfree = 0
print(myList)

def AddItem(newItem):
    global nextfree
    global start
    if nextfree == -1:
        print("The list is full")
    else: 
        myList[nextfree].name = newItem
        if start == -1:
            temp = myList[nextfree].pointer       #save pointer
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:  
                myList[nextfree].pointer = start
                start = nextfree
            else:    
                placeFound = False    #general case
                while myList[p].pointer != -1 and placeFound == False:
                    if newItem >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placeFound = True
                temp = nextfree
                nextfree = myList[nextfree].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp

AddItem("Hello")
AddItem("Hi")
AddItem("How are you")
AddItem("Yello")
AddItem("Sup")
AddItem("ASDKoasDKads")
print(myList)