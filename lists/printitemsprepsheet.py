class fruity:
    def __init__(self,nane,ponter):
        self.name = nane                    #has to be different than atribute
        self.pointer = ponter
    #end constructor
    def __repr__(self) -> str:
        return f'(Name: {self.name}; Pointer: {self.pointer})'
    #endfunction
#endclass
fruit = [fruity("",x+1) for x in range(5)]
fruit.append(fruity("",-1))
fruit[0].name = "Banana"
fruit[1].name = "Strawberry"
fruit[2].name = "Melon"
fruit[3].name = "Lemon"
fruit[4].name = "Blueberry"
fruit[0].pointer = 4
fruit[1].pointer = -1
fruit[2].pointer = 1
fruit[3].pointer = 2
fruit[4].pointer = 3
start = 0 
length = 0  
point = start
print(fruit[point].name) 
while point < -1 or point > -1: 
    print(fruit[fruit[point].pointer].name)  
    point = fruit[point].pointer  
    length = length + 1  
#endwhile  
print(length) 
