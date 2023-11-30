class Node:
    def __init__(self, name, pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
    #end Node record

myList = [Node("", -1) for _ in range(5)]
for index in range(4):
    myList[index].pointer = index + 1
    #myList[index].name = "0" + str(index)
myList[4].pointer = -1

print(myList)

