number = [34, 36, 39, 45, 48, 50, 53, 57, 69, 71, 73] 
def binary_search(array, target):
    l = 0
    r = len(array)
    m = int((l + r) / 2)
    found = True    
    index = -1
    while found == False:
        if target == array[m]:
            found = True
        elif target < array[m]:
            l = l
            r = m
            m = int((l + r)/2)
        elif target > array[m]:
            l = m
            r = r
            m = int((l + r)/2)
    index = target
    return index
print(binary_search(number, 39))

