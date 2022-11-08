class NodeType:
    def _init_(self):
        self.name = ""
        self.pointer = -1
    #end constructor    
#endclass

x = NodeType()
x.name = "Ava"
x.pointer = 0
print(x.name, x.pointer)

myList = [NodeType() for _ in range(50)]

for node in myList:
    print(node.pointer)