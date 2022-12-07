import os
import random
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
line = f.read().splitlines()
data = random.choice(line)
print(data)
#It works!