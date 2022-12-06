import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
data = f.read().split()
max = len(max(data, key=len))
for i in data:
    if len(i) == max:
        word = i
print(word)
#It works!