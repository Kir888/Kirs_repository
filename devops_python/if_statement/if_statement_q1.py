limit_IN = 70
limit_US = 55


print("Please enter your state")
state_of_driver = input()

print("Please enter your speed")
speed_of_driver = (input())


is_in_IN = state_of_driver == "IN"

if is_in_IN and speed_of_driver <= limit_IN or (not is_in_IN and speed_of_driver <= limit_US):
    print("You are driving safe!")
elif is_in_IN and speed_of_driver <= (limit_IN + 0.1*limit_IN):
    print("YELLOW WARNING")
elif not(is_in_IN) and speed_of_driver <= (limit_US + 0.1*limit_US):
    print("CITATION")
elif is_in_IN and speed_of_driver > (limit_IN + 0.1*limit_IN):
    print("$150 and 5 points")
elif not(is_in_IN) and speed_of_driver > (limit_US + 0.1*limit_US):
    print("$100")
