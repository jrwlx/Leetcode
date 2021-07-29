from math import inf

def func(nums, target):
    window_start = 0
    window_sum = 0
    min_length = inf
    for window_end in range(len(nums)):
        window_sum += nums[window_end]

        while window_sum >= target:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= nums[window_start]
            window_start += 1

    if min_length == inf:
        return 0

    return min_length