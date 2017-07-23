def multiplyTwoStrings(s1, s2):
    multi = [0] * (len(s1) + len(s2) - 1)
    res = ''
    # chinese/japanese method of multiplication
    for i2, v2 in enumerate(s2):
        for i1, v1 in enumerate(s1):
            multi[i1 + i2] += int(v2) * int(v1)

    # moving tenthes and filling result string
    for i in range(len(multi) - 1, 0, -1):
        v = multi[i]
        multi[i - 1] += v // 10
        res = str(v % 10) + res
    return str(multi[0]) + res

print(multiplyTwoStrings('15','17'))