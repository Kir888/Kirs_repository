d1 = {
    "brand":"Apple",
    "model": "Macbook Pro",
    "year":2021
}

d1.pop("brand")
print(d1)
d1.update({"brand2":"Windows"})
print(d1)
d1.popitem()
print(d1)

#del keyword

del d1["model"]
print(d1)

#removing all dictionary

print(d1) #error, everything is removed