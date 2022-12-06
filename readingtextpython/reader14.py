import os
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\readingtextpython')

f = open('nd.txt', 'r', encoding="utf8")
t = open('exoeriment.txt', 'r', encoding="utf8")
list1 = f.readlines()
list2 = t.readlines()
string = ""
if len(list1) > len(list2):
    for i in range(0,len(list2)):
        line1 = str(list1[i])
        line2 = str(list2[i])
        string = line1 + line2
        print(string)
else:
    for i in range(0,len(list1)):
        line1 = str(list1[i])
        line2 = str(list2[i])
        string = line1 + line2
        print(string)
#It works!