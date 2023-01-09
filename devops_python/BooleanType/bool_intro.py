bool1 = True
bool2 = False

print(type(bool1)) #<class 'bool'>
print(type(bool2)) #<class 'bool'>

# We are trying to use arithmetical operation
print(bool1 + 6) # '7'

print(bool2 * 112) # 0

# what happens when we use comma between a number and boolean variable.

print(bool1,"text") #True 6
print(bool2, 6) #False 6

# How to print string and boolean in single print function
# Just use comma between two variable.
print("The value of the bool1 is", bool1)
print("The value of the bool2 is", bool2)