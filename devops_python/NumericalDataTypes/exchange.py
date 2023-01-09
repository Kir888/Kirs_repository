

qarter = 25 
nickel = 5
dime = 10
penny = 1
exchange = 8.04
total_cents = int(exchange * 100)
count_of_q = (total_cents // qarter)
left_after_q = (total_cents % qarter)
count_of_d = (left_after_q // dime)
left_after_d = (left_after_q % dime)
count_of_n = (left_after_d // nickel)
count_of_p = (left_after_d % nickel)


print(count_of_q, count_of_d, count_of_n, count_of_p)