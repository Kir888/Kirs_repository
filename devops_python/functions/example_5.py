#Create a method that will take one list as a parameter and one positive integer
#index as a parameter. Return the negative index for given positive index number.

def find_negative(s1,index):
    neg_index = index - len(s1)
    return neg_index
print(find_negative(["p", "y", "t", 3, "y"],3))
