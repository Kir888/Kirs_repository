a = "Python"


print(a.find("h"))

var2 = "Encapsulation is good for data hiding"

print(var2.find("a"))
#Even character is repeating through out the
#string it will return index number of first character

#rfind() method
#This method will help us to get
# lat position of a given character
print(var2.rfind("a")) #29

var3 = "Python Python"

print(var3.find("hon"))

#3
#even in muptiple characters it will return first index number

print(var3.find("Peter"))  # -1 if it cant find index number

print(var3.find("z")) # -1

print(var3.rfind("th")) #9

var4 = "Programming"

print(var4.find("Programming"))