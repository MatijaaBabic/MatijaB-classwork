gnames = ["Amelia","Olivia","Isla","Emily","Poppy", "Ava","Isabella","Jessica","Lily","Sophie"]
def search(list, item):
    index = -1
    i = 0
    found = False
    while i < len(list) and found == False:
        if list[i] == item: #then
            index = i
            found = True
        #endif
        i = i + 1
    #endwhile
    return index
#endprocedure
print(search(gnames, "Lily"))
print(search(gnames, "Ada"))    