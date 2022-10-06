numbers = []

for _ in range (6):
    numbers.append(int(input("Enter num: ")))
#next _
total = 0
avg = 0
for index in range(5,-1,-1):         #we can use in range(5,-1,-1)
    print(numbers[index])                 
    total = total + numbers[index]
    avg = total / 6  
#next index
print(total, "total")
print("average", avg)      