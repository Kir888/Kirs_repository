d1 = {
    "brand":"Apple",
    "model": "Macbook Pro",
    "year":2021
}

d1["model"] = "Macbook Air"

d1["new"] = "Macbook Pro" # to add
print(d1)

d1.update({"year":2022})
print(d1)

d1.update({"charging-port":"usb"})
print(d1)