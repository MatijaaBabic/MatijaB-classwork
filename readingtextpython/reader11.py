import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = "nd.txt"
f_size = os.stat(f)
print(f_size.st_size, "bytes")
#It works!