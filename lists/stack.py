myString = input("Please enter a word or phrase to be tested: ") 
list1 = list(myString)   #convert myString to a list of characters 
numChars = len(list1) 
s = list("") 
item = "" 
for index in range (0, len(list1)): 
    item = list1[(len(list1)-1)-index] 
    s.append(item)
#next index  
#print(item)
#print(s)
#print(list1)
if s == list1: #then
    print("The word is a palindrome") 
else: 
    print("The word isn't a palindrome") 
#endif 