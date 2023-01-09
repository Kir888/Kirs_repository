#remove suffix -> will remove it from end of the string
#remove preffix will remove it from beginning of the string

s = "Hello World"

print(s.removeprefix("World")) # Hello World

print(s.removeprefix("Hello")) #_World

print(s.removesuffix("World")) # Hello_

print(s.strip("elloH")) # _Wor