list1 = [2,5,15,36,47,56,59,78,156,244,268] 
list2 = [18,39,42,43,66,69,100] 
mergeList = [] 
x = 0 
y = 0 
index1 = 0 
index2 = 0 
while index2 != (len(list2)): 
    if list1[index1] <= list2[index2]: #then 
        x = list1[index1] 
        mergeList.append(x) 
        index1 = index1 + 1 
    else: #then 
        Y = list2[index2] 
        mergeList.append(Y) 
        index2 = index2 + 1 
    #Endif 
#Endwhile 
for index1 in range (index1, (len(list1))): 
    x = list1[index1] 
    mergeList.append(x) 
#Endfor 
print(mergeList) 