a = [1, 3, 2, 6, 7, 4, 9, 8]
b = [33, 51, 514, 61432, 3]
c = ["c", "g", "e", "s", "z","m"]
def bubble(array):
    for x in range(0, len(array)-1):
        swap = True
        for y in range(0, len(array)-1-x):
            if array[y] > array[y+1]:
                temp = -1
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
    return array
print(bubble(a))
print(bubble(b))
print(bubble(c))
                