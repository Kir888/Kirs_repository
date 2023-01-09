s = {1,2,3,4}
s1 ,s2, *s3 = s
print(s3)

set = {1,2,3,4}
for a in set:
    print(a)

set = {1,2,3,4}
print(3 in set) # True because 3 in the loop
print(5 in set) # False, because there is no 5 in the set

s.add(7)
print(s)

s1 = {1,2,3}
s2 = {5,"fds", "fsaf"}
s1.update(s2)
print(s2)