import time
def bubblesort(arr):
    for x in range(0, len(arr)-1):
        swap = True
        for y in range(0, len(arr)-1-x):
            if arr[y] > arr[y+1]:
                temp = -1
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp
    return arr

def insertsort(arr):
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6, 7, 2, 5, 10, 32]
arr1 = [12, 11, 13, 5, 6, 7, 2, 5, 10, 32]
bubblesort(arr1)
insertsort(arr)
print(arr)