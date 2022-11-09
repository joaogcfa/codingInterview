BITS = 32  # Assuming 32-bits


def longest_sequence(n):
    if ~n == 0:
        return BITS

    current_length = 0
    previous_length = 0
    max_length = 1

    for i in range(BITS):
        if (n & 1) == 1:
            current_length += 1
        elif (n & 1) == 0:
            previous_length = 0 if (n >> 2) == 0 else current_length
            current_length = 0
        max_length = max(previous_length + current_length + 1, max_length)
        n >>= 1

    return max_length


print(longest_sequence(1775))
