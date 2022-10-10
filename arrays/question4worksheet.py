outlets, quarters = (50, 4)
outletSales= [[0 for i in range(quarters)] for j in range(outlets)]
print(outletSales)
total = [5, 13, 45, 12]
for quarter in range(quarters):
    total[quarter] = 0                  #defining total in a loop
    for outlet in range(outlets):
        total[quarter] = total[quarter] + outletSales[outlet][quarter]
    #next outlet
    print("Quarter,", quarter+1, "Total is", total[quarter])
#next quarter 