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
sp = -1
nf = 0
def AddItem(newName):
    global sp
    global nf
    if myList[nf].pointer  == -1: #then #check if the list is full
        print("Error: List full") 
    else:                   
        myList[nf].name = newName
        if sp == -1:                      #check if list is empty
            temp = myList[nf].pointer       
            myList[nf].pointer = -1
            sp = nf
            nf = temp
        else:
            p = sp
            if newName < myList[p].name:         #check if the new name is alphabetically before the starting name
                myList[nf].pointer = sp
                sp = nf
            else:                                #this part of the code is completely confusing to me, I attempted to make the part above into a for loop so that it works for all words instead just for the first one but it messed up the results further. Biggest issue = me stressing myself * my lack of knowledge 
                placeFound = False
                while myList[p].pointer != -1 and placeFound == False:
                    if newName >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placeFound = True
                    #endif
                #endwhile
                #temp = nf
                temp = myList[nf].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp
                nf = temp
            #endif
        #endif
    #endif
#endprocedure
AddItem("Matija")
AddItem("John")
AddItem("E")
print(myList)
print(sp)
print(nf)