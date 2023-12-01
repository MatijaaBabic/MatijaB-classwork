class Stack:
    #private start
    #public max

    #public constructor(maxSize)
    def __init__(self, maxSize):
        self.data = ["" for _ in range(maxSize)]       
        self.sp = -1          
        self.max = maxSize      
    #end constructor

    def __repr__(self) -> str:
        blank = ''
        for item in self.data:
            blank += item + '\n'
            return blank


    def isFull(self):               #public function isFull():
        return self.sp == self.max - 1
    #end function

    #public function isEmpty()
    def isEmpty(self):
        return self.sp == -1
    #end function

    #public procedure findNumOfItem()
    def findNumOfItem(self):
        return (self.sp + 1)
    #end procedure

    #public function findLastLoc()
    def findLastLoc(self):
        return self.sp
    #end function

    #public function peek()
    def peek(self, index):
        return self.data[index]
    #end function

    #public procedure push
    def push(self, item):
        if self.isFull() == True:
            print("Not enough space")
        else:
            self.sp = self.sp + 1
            self.data[self.sp] = item
        #endif
    #end procedure

    #public function pop()
    def pop(self):
        if self.isEmpty() == True:
            print("No items in the stack")
        else:
            temp = self.sp
            self.sp = self.sp - 1
            return self.data[temp]
        #endif
    #end function


stack = Stack(11)
stack.push("Y")
print(stack)


print(stack.isEmpty())

for i in range(5):
    print(stack.pop())
