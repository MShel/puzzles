def memorize(f):
    cache = {}

    def mem(key):
        if key not in cache:
            cache[key] = f(key)
        return cache[key]

    return mem


'''
recursive approach, nice but my cause stuck overflow
'''
def mapDecoding(string):
    if len(string) > 0 and int(string) == 0:
        return 0
    if not validate_string(string):
        return 0

    @memorize
    def get_branches(string):
        if not string or len(string) == 1:
            return 0
        if string[0:2] <= '26':
            if '0' not in string[1:3]:
                return 1 + get_branches(string[1:]) + get_branches(string[2:])
            else:
                return get_branches(string[2:])
        else:
            return get_branches(string[1:])

    result = (1 + get_branches(string)) % (10 ** 9 + 7)
    return result


def validate_string(string):
    if '00' in string:
        return False

    for char_index in range(0, len(string) - 1):
        if int(string[char_index]) > 2 and int(string[char_index + 1]) == 0:
            return False

    return True

'''
better solution with 
O(n) time
O(n) space wo memorisation... with would be O(1)... to memorize we can turn add dict to collect results
'''
def map_decoding1(string):
    all_combinations_counts = [0 for _ in range(0, len(string)+1)]
    all_combinations_counts[0] = 1
    for i in range(1, len(string)+1):
        current_char = string[i - 1]
        prev_char = string[i - 2] if i > 1 else None

        if current_char == '0' and prev_char == '0':
            return 0

        all_combinations_counts[i] = 0

        if current_char != '0':
            all_combinations_counts[i] += all_combinations_counts[i - 1]
        elif prev_char and int(prev_char) > 2:
            return 0

        if prev_char != None and prev_char != '0' and int(prev_char + current_char) <= 26:
            all_combinations_counts[i] += all_combinations_counts[i - 2]

    result = all_combinations_counts.pop() % (10 ** 9 + 7)
    return result


test = "123"

print(map_decoding1(test))
