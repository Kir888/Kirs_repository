nums = [1,2,2,3,1,2,3,4,4]
index = 0

while index < len(nums):
    if nums[index] == 2:
        nums.remove(2)
        index -=1
    index += 1
print(nums)