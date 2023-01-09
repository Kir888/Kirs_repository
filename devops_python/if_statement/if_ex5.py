print("Enter the kilogram amount of shipment")
goal_ship = int(input())
print("Enter amount of small packages you have")
count_of_small = int(input())
print("Enter amount of big packages you have")
count_of_big = int(input())

big_packages_needed = goal_ship // 5

if count_of_big >= big_packages_needed:
    needed_small_packages = goal_ship % 5
    if count_of_small >= needed_small_packages:
     print(f"I can do the shipment and I need {needed_small_packages} small packages")
    else:
     went_over = 5 - count_of_small
     print("I can do the shipment because,")
     print(f"We didn't have enough packages so we went over {went_over} kgs")
    
elif count_of_big < big_packages_needed:
   kg_I_have = count_of_big * 5
   needed_small_packages = goal_ship - kg_I_have
   if count_of_small >= needed_small_packages:
    print(f"I can do the shipment and I need {needed_small_packages} small packages")
   else:
    print("I can't do the shipment because,")
    print(f"I need {needed_small_packages} small packages but, I have {count_of_small} packages")
