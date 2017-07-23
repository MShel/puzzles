from operator import itemgetter
from copy import copy
import random
from collections import deque

from heapq import heappop, heappush
import cProfile

def genSolutions(coins):
    coins = sorted(coins, key=itemgetter(0, 1), reverse=True)
    #list to store all the results
    score_storage = deque([])
    # will use dictionary to make we did not already record this cell
    dict_helper = {}
    for coin in coins:
        full_score_storage = copy(list(score_storage))
        new_storage, index = update_solutions_dict(coin, score_storage, dict_helper)

        if new_storage:
            try:
                old_largest_elem_score = full_score_storage[0][2]
                old_smallest_elem_score = full_score_storage[len(full_score_storage)-1][2]
                if new_storage and new_storage[0][2] > old_largest_elem_score:
                    full_score_storage.insert(0, new_storage[0])
                    score_storage = deque(full_score_storage)
                elif new_storage and new_storage[0][2] < old_smallest_elem_score:
                    full_score_storage.append(new_storage[0])
                    score_storage = deque(full_score_storage)
                else:
                    full_score_storage.insert(index, new_storage[0])
                    score_storage = deque(full_score_storage)
            except IndexError:
                full_score_storage.insert(index, new_storage[0])
                score_storage = deque(full_score_storage)
        else:
            score_storage = deque(full_score_storage + new_storage)
    return list(score_storage)

def update_solutions_dict(coin, score_storage, dict_helper,index = 0):
    try:
        new_storage = []
        latest_biggest_solution = get_biggest_solution(score_storage)
        score = latest_biggest_solution[2] + 1

        if latest_biggest_solution[0] - coin[0] >= 0 and latest_biggest_solution[1] - coin[1] >= 0:
            if not (coin[0],coin[1]) in dict_helper:
                new_storage.append([coin[0], coin[1], score])
                dict_helper[(coin[0], coin[1])] = score

            return new_storage,index
        else:
            index += 1
            return update_solutions_dict(coin, score_storage, dict_helper,index)
    except Exception:
        if not (coin[0], coin[1]) in dict_helper:
            dict_helper[(coin[0], coin[1])] = 1
            new_storage.append([coin[0], coin[1], 1])
        return new_storage,index


def get_biggest_solution(score_storage):
    return score_storage.popleft()


def maximizeCoins(coins):
    coins_solutions = genSolutions(coins)
    prev_coin = [0, 0]
    counter = 0
    while coins_solutions:
        coin = coins_solutions.pop(0)

        if coin[0] - prev_coin[0] >= 0 and coin[1] - prev_coin[1] >= 0:
            counter += 1
            prev_coin = coin

    return counter

coins = []
i = 0
while i < 20000:
    coins.append([random.randint(0, 40), random.randint(0, 40)])
    i += 1
#coins = [[0,1],
# [1,1],
# [2,0],
#[1,2],
#[2,2]]
#print(maximizeCoins(coins))
print(cProfile.run('maximizeCoins(coins)'))
