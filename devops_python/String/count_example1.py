print("Enter a string that consist of dog adn cat words")
str = input()

count_of_dogs = str.count("dog")

count_of_cats = str.count("cat")

is_counts_same = count_of_cats == count_of_dogs

print(is_counts_same)

