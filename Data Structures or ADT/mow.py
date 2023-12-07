f = open('mow.txt', 'r')
data = f.read()
f.close()
print(data)

mow = {}

wordStart = False
for c in data:
    if 96 < ord(c.lower()) < 123:
        if not wordStart:
            wordStart = True
            word = c.lower()
        else: 
            word += c.lower()
    else: 
        if wordStart:
            wordStart = False
            if word in mow:
                mow[word] += 1
            else:
                mow[word] = 1

print(mow)
#findWord = input("Which word do you want to find: ")


#if findWord in mow:
#    print(mow[findWord])
#else:
#    print("Word not recognised")

print("The size of the dictionary: ", str(len(mow)))
print("meadow" in mow)
print(mow["five"])

def remove(dictionary, remove):
    if remove in dictionary:
        del remove
        return True
    else:
        return False




removeWord = input("Which word do you want to remove: ")

print(remove(mow, removeWord))
