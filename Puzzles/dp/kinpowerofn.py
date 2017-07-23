import cProfile


def dumb_k_in_power_of_n(number, n):
    if n < 0:
        number = 1 / number
        n = -n

    if n == 0:
        return 1

    result = number
    counter = 1

    while counter < n:
        result = result * number
        counter += 1

    return result


'''
Exponentiation by squaring
'''
def k_in_power_of_n(number, n):
    if n < 0:
        number = 1 / number
        n = -n

    if n == 0:
        return 1

    y = 1
    while n > 1:
        if n % 2 == 0:
            number = number * number
            n = n / 2
        else:
            y = number * y
            number = number * number
            n = (n - 1) / 2
    return number * y



print(dumb_k_in_power_of_n(2, 9))
print(k_in_power_of_n(2, 9))
