number = [34, 36, 39, 45, 48, 50, 53, 57, 69, 71, 73] 
def binary_search(list, target): 
      found = False 
      index = -1 
      f = 0 
      l = len(list)
      while f <= l and found == False:
         mid = (f + l) // 2 
         if list[mid] == target:
           found = True
           index = mid
         else:  
           if list[mid] < target:
              f = mid + 1
           else:
              l = l -1                         
      return index                                
print(binary_search(number, 36))
print(binary_search(number, 69))
print(binary_search(number, 40))
