import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
n = int(input("How many last lines do you want to read: "))
lineList = f.readlines()
for i in range(0, n):
    data = lineList[len(lineList)-(n-i)]
    print(data)

#It works!