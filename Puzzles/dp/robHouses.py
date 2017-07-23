test_houses = [1,2,3,4,5,6,100]

def house_robber(street:list)->int:
    if len(street) == 0:
        return 0

    if len(street) == 1:
        return street[0]

    if len(street) == 2:
        return  max(street[0], street[1])

    valueToSteal1 = street[0] + house_robber(street[2:])
    valueToSteal2 = house_robber(street[1:])

    return max(valueToSteal1,valueToSteal2)

def house_robber1(street:list)->int:
    oldBest, newBest = 0,0
    for currValue in street:
        take = currValue + oldBest
        oldBest = newBest
        newBest = max(take, oldBest)
    return newBest

assert house_robber(test_houses) == 109, "Invalid amount returned"
assert house_robber1(test_houses) == 109, "Invalid amount returned"

