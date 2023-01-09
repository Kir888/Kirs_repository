str1 = "Snicker"
str1 = str1.strip("rS").upper().removeprefix("N")[:2] 
print(str1)
str2 = "Cookie"
str2 = str2.lower().replace("o","u").removesuffix("e").startswith("C")
print(str2)