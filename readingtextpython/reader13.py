import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('reader12.txt', 'r', encoding="utf8")
data = f.readlines()
t = open('reader13.txt', 'w', encoding="utf8")
for i in range(0, len(data)):
    t.write(data[i])
#It works!