def func(s, k):
    freq = {}
    largest_letter_freq, window_start, max_length = 0, 0, 0

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char not in freq:
            freq[right_char] = 0
        freq[right_char] += 1

        largest_letter_freq = max(largest_letter_freq, freq[right_char])

        while (window_end - window_start + 1) > largest_letter_freq + k:
            left_char = s[window_start]

            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
