
def func(nums):
    left = 0
    right, highest_index = len(nums) - 1, len(nums) - 1
    output_arr = [0] * len(nums)

    while left <= right:
        leftput = nums[left] * nums[left]
        rightput = nums[right] * nums[right]

        if leftput > rightput:
            output_arr[highest_index] = leftput
            left += 1
        else:
            output_arr[highest_index] = rightput
            right -= 1

        highest_index -= 1

    return output_arr
