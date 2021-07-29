
def func(fruits):
    freq = {}
    window_start, max_length = 0, 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in freq:
            freq[right_fruit] = 0
        freq[right_fruit] += 1

        while len(freq) > 2:
            left_fruit = fruits[window_start]
            freq[left_fruit] -= 1
            if freq[left_fruit] == 0:
                del freq[left_fruit]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

