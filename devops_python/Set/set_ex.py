l = ["n","1",1,2,3]
l2 = ["n",3,"1",10,11,"new","n","1",3]
list_of_elements = []
for element in l:
    if element in l2:
        list_of_elements.append(element)
print(list(set(list_of_elements)))

l = ["n","1",1,2,3]
l2 = ["n",3,"1",10,11,"new","n","1",3]
s1 = set(l)
s2 = set(l2)
s3 = s1.intersection(s2)
l = list(s3)
print(l)