class NodeType:
    def __init__(self,nane,ponter):
        self.name = nane                    #has to be different than atribute
        self.pointer = ponter
    def __repr__(self) -> str:
        return f'(Name: {self.name}; Pointer: {self.pointer})'
    #end constructor
myList = [NodeType("",x+1) for x in range(9)]
myList.append(NodeType("",-1))
for index in range (0,8):
	myList[index].pointer = index + 1
myList[9].pointer = -1
newName = str(input("Please input the name wanted: "))
def AddItem(newItem):
    start = -1
    nextfree = 0
    if myList[nextfree].pointer  == -1: #then 
        print("Error: List full") 
    else:
        myList[nextfree].name = newName
        if start == -1:
            temp = myList[nextfree].pointer       
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:
                myList[nextfree].pointer = start
                start = nextfree
            else:
                placeFound = False
                while myList[p].pointer != -1 and placeFound == False:
                    if newItem >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placefound = True
                    #endif
                #endwhile
                temp = nextfree
                nextfree = NodeType[nextfree].pointer
                NodeType[temp].pointer = NodeType[p].pointer
                NodeType[p].pointer = temp
            #endif
        #endif
    #endif
#endprocedure
AddItem(newName)
print(myList)