print("enter a sentence")
sentence = input()
list = sentence.split(" ")

print(list)
count_of_words = len(list)
print(count_of_words)

count_of_space = sentence.count(" ")
print("Comes from count of space +1 ", count_of_space +1)