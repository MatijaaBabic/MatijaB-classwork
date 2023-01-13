
def bubblesort(array):
    for x in range(0, len(array)-1):
        swap = True
        for y in range(0, len(array)-1-x):
            if array[y] > array[y+1]:
                temp = -1
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
    return array

def insertsort(array):
    