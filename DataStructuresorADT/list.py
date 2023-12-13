
class CustomString(str):
    def custom_method(self):
        return f"Custom method called on {self}"
    
    def toggle(self):
        list1 = ""
        for i in self:
            list1 += (chr(ord(i) ^ 0b00100000)) 
        return str(list1)
    
    def find_character(self, want):
        string1 = list(self)
        for i in range (0, len(string1)):
            if string1[i] == want:
                return want 

x = CustomString("hello")
print(x)
print(x.toggle())
find = str(input())
print(x.find_character(find))