import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
lineList = f.readlines()
poem = []
for i in range(0, len(lineList)):
    poem.append(lineList[i])
print(poem)
#It works!