
var1 = "Techtorial Academy"

print(var1.isalpha())
#False
#Spaces are not cosidered as letters
#therefore, this will return False.
print(var1.replace(" ","").isalpha())

var2 = "Weatherisniceoutside."
print(var2.isalpha()) #False (dot)

var3 = "1234567"

print(var3.isnumeric())

var4 = "1.5"
print(var4.isnumeric())
#False    

#isalnum
#It'll return True when string contains letters and numbers
var5 = "Phonenumberis"
print(var5.isalnum())
#True

var6 = "#777777"
print(var6.isalnum())
#False, because # is neither number nor letter