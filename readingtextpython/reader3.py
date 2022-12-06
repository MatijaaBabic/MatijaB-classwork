import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')
f = open("exoeriment.txt", 'a')
data = "Hello, World!"
data2 = "Atari is the best!"
f.write(data)
f.write(data2)
f = open("exoeriment.txt", 'r')
print(f.read())

#var = f.readline()
#print(var)
#It works!