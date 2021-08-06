
def func(nums, k):
    prod = 1
    res = 0
    window_start = 0
    for window_end in range(len(nums)):
        prod *= nums[window_end]

        while prod >= k and window_start <= window_end:
            prod /= nums[window_start]
            window_start += 1

        res += window_end - window_start + 1

    return res