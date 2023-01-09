dollars = 12.45

cents = int(dollars * 100)

quarter = 25
dime = 10
nickel = 5
penny = 1
count_of_q = cents // quarter
count_of_d = cents % quarter // dime
count_of_n = cents % quarter % dime // nickel
count_of_p = cents % quarter % dime % nickel

print(dollars, "will make", count_of_q, "qarters", count_of_d, "dimes", 
count_of_n, "nickels", count_of_p, "pennies" )