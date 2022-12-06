import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')
f = open("nd.txt", 'r')
n = int(input("Input the number of lines you want to read: "))
for i in range(0,n):
    variable = f.readline()
    print(variable)

#It works!