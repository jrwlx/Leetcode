
def func(s1, s2):
    freq = {}
    matched, window_start = 0, 0

    for letter in s1:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1

    for window_end in range(len(s2)):
        right_char = s2[window_end]
        if right_char in freq:
            freq[right_char] -= 1
            if freq[right_char] == 0:
                matched += 1

        if matched == len(freq):
            return True

        while (window_end - window_start + 1) >= len(s1):
            left_char = s2[window_start]
            if left_char in freq:
                if freq[left_char] == 0:
                    matched -= 1
                freq[left_char] += 1
            window_start += 1

    return False