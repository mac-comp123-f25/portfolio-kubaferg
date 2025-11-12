def every_other (list):
    return list [::2]
print(every_other([2,4,6,8,10]))

def sum_positive (nums):
    total = 0
    for num in nums:
        if num > 0:
            total += num
    return total
print(sum_positive([2,-4,6,-8,10]))