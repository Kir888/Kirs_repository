#create a method to find highest common factor of two given number.
#highest common factor is a biggest common divisor of two given numbers.
# 24 18 ->6
def highest_common_factor(n1,n2):
    #if it can divide both numbers without any remainder
    hcf = n1
    while n1%hcf == 0 and n2 % hcf == 0:
        hcf-=1
    return hcf
print(highest_common_factor(18,24))