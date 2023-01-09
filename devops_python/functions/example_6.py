def exist_value(dict,value1):
    return value1 in dict.keys()
d = {
    "name" : "y",
    "last_name" : "t",
    "school_num":390,
}
print(exist_value(d,"name"))
print(exist_value(d,210))