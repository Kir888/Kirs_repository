nums = [1,2,10,11,13,17,21,26]

index = 0
sum = 0
while index <= len(nums) -1:
    if nums[index] % 2 != 0:
        sum = nums[index] + sum
    index += 1
print(sum)
