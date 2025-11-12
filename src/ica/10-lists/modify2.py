def remove_all (value, lst):
    while lst.count(value)>0:
        lst.remove(value)
nums = [3,8,9,4,5,2,3]
remove_all(3, nums)
print(nums)