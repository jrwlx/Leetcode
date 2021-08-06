
def func(nums):
    left = 0
    right = len(nums) - 1
    index = 0

    while index <= right:
        if nums[index] == 0:
            nums[index] = nums[left]
            nums[left] = 0
            left += 1
            index += 1
        elif nums[index] == 2:
            nums[index] = nums[right]
            nums[right] = 2
            right -= 1
        else:
            index += 1