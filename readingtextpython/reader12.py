import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')
line = ["a", "b", "c", "d", "e"]
f = open('reader12.txt', 'w', encoding="utf8")
for i in range(0, len(line)):
    f.write(line[i])


#It works!