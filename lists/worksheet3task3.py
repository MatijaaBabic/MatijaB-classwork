list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
templist = []
x = 0
y = 0
index1 = 0
index2 = 0
while index2 != (len(list2)):
    if list1[index1] <= list2[index2]: #then
        x = list1[index1]
        templist.append(x)
        index1 = index1 + 1
    else: #then
        x = list2[index2]
        templist.append(x)
        index2 = index2 + 1
    #endif
#endwhile
for index in range (index1, len(list1)):
    y = list1[index1]
    templist.append(y)
#endfor
print(templist)
