bool1 = True
bool2 = False

print(bool1 and bool2) #False

print(bool1 and not bool2) #True

print(bool1 or bool2) #True

print(not bool1 or bool2) #False

age_of_kid, required_age =7, 11

can_participate = age_of_kid <= required_age

print("The kid can participate", can_participate)
walk = 6700
run = 4
eat = 1499
vera_loses_weight = (run >= 4 or walk >= 10000) and eat < 1500

print("Veera can loose weight", vera_loses_weight)

a = 5
b = 8
c = 15

(print(a >= 5 or b <=7 and c == 15))