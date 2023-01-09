names = input("type your names ")
list = names.split(", ")
import random
rndm_number = random.randint(0, len(list)-1)
print(list[rndm_number] + " is going to buy the meal today")