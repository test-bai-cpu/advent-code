import sys

#COUNT = 0

def count_eight(nums):
    if COUNT > 80:
        print(COUNT)
        sys.exit(1)
    new_nums = []
    for num in nums:
        if num > 0 and num < 9:
            new_nums.append(num - 1)
        elif num == 0:
            new_nums.append(8)
            new_nums.append(6)
    count_eight(new_nums)
    COUNT += 1

#count_eight([1])


def dp(days, nums):
    count = 0
    while (count < days):
        new_nums = []
        for num in nums:
            if num > 0 and num < 9:
                new_nums.append(num - 1)
            elif num == 0:
                new_nums.append(8)
                new_nums.append(6)
        count += 1
        nums = new_nums
    return len(nums)



print(dp(256, [1]))
