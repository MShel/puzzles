from operator import itemgetter
from copy import copy
import random
from collections import deque


def genSolutions(coins):
    coins = sorted(coins, key=itemgetter(0, 1), reverse=True)
    # list to store all the results
    score_storage = deque([])
    # will use dictionary to make sure we did not already record this cell
    dict_helper = {}
    for coin in coins:
        full_score_storage = copy(score_storage)
        new_storage, index = update_solutions_dict(coin, score_storage, dict_helper)

        if new_storage:
            try:
                largest = full_score_storage[0]
                smallest = full_score_storage[-1]
                old_largest_elem_score = largest[2]
                old_smallest_elem_score = smallest[2]
                if new_storage and new_storage[0][2] > old_largest_elem_score:
                    full_score_storage.appendleft(new_storage[0])
                    score_storage = full_score_storage
                elif new_storage and new_storage[0][2] < old_smallest_elem_score:
                    full_score_storage.append(new_storage[0])
                    score_storage = full_score_storage
                else:
                    full_score_storage = list(full_score_storage)
                    full_score_storage.insert(index, new_storage[0])
                    score_storage = deque(full_score_storage)
            except IndexError:
                full_score_storage.append(new_storage[0])
                score_storage = full_score_storage
        else:
            score_storage = full_score_storage + deque(new_storage)
    return score_storage


def update_solutions_dict(coin, score_storage, dict_helper, index=0):
    try:
        new_storage = []
        latest_biggest_solution = get_biggest_solution(score_storage)
        score = latest_biggest_solution[2] + 1

        if latest_biggest_solution[0] - coin[0] >= 0 and latest_biggest_solution[1] - coin[1] >= 0:
            if not (coin[0], coin[1]) in dict_helper:
                new_storage.append([coin[0], coin[1], score])
                dict_helper[(coin[0], coin[1])] = score

            return new_storage, index
        else:
            index += 1
            return update_solutions_dict(coin, score_storage, dict_helper, index)
    except Exception as e:
        if not (coin[0], coin[1]) in dict_helper:
            dict_helper[(coin[0], coin[1])] = 1
            new_storage.append([coin[0], coin[1], 1])
        return new_storage, index


def get_biggest_solution(score_storage):
    return score_storage.popleft()


def maximizeCoins(coins):
    counter = 0
    coins_solutions = genSolutions(coins)

    prev_coin = [0, 0]
    while coins_solutions:
        coin = coins_solutions.popleft()
        if coin[0] - prev_coin[0] >= 0 and coin[1] - prev_coin[1] >= 0:
            counter += 1
            prev_coin = coin

    return counter

coins = [[0,0],[0,0],[0,0]]
for i in range(0, 10000):
   coins.append([random.randint(0, 100), random.randint(0, 100)])

print(maximizeCoins(coins))
#cProfile.run('maximizeCoins(coins)')
