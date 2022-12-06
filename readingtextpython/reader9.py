import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
lineList = f.readlines()
for i in range(0, len(lineList)):
    data = lineList[i]
    num = list(data)
    length = len(num)
    print(length)
#It works!