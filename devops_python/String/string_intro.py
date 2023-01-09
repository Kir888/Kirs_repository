# Create a string variable

a = "hello"

b = "hello "

# we can use == sign to compare two strings

print(a == b) #False

c = "Hello" 
print(a == c) #False, because the case matters

print(a == "hello") #True 

[print ('hello' == "hello")] #True

# Strings are immutable

string = "fsafasjkg"

last_index = len(string) -1

print(string[last_index])