
def remove_duplicates(nums):
    next_nonduplicate = 1
    i = 1
    while i < len(nums):
        if nums[next_nonduplicate - 1] != nums[i]:
            nums[next_nonduplicate] = nums[i]
            next_nonduplicate += 1
        i += 1
    return next_nonduplicate

