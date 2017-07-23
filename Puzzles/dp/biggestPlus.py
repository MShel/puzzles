def memorize(f):
    cache = {}

    def mem(column, matrix):
        if column not in cache:
            cache[column] = f(column, matrix)
        return cache[column]

    return mem


def biggestPlus(matrix: list) -> int:
    #relevant_indexes = getRelevantIndexes(matrix)
    result = []
    left_cache = {}
    right_cache = {}
    top_cache = {}
    bottom_cache = {}

    row_index = 0
    for row in matrix:
        column_index = 0
        for column in row:
            column_index += 1
            if column == '1':
                min_rank = test_left(column_index-1, row, row_index, left_cache)
                if min_rank == 0:
                   continue

                new_min_rank = test_right(column_index-1, row, row_index, right_cache)
                if new_min_rank < min_rank:
                    min_rank = new_min_rank

                if min_rank == 0:
                    continue
                new_min_rank = test_top(row_index, get_column(column_index-1, matrix),column_index,top_cache)

                if new_min_rank < min_rank:
                    min_rank = new_min_rank

                if min_rank == 0:
                    continue

                new_min_rank = test_bottom(row_index, get_column(column_index-1, matrix),column_index,bottom_cache)
                if new_min_rank < min_rank:
                    min_rank = new_min_rank
                if min_rank == 0:
                    continue

                result.append(min_rank)
        row_index += 1
    if not result:
        result = 0
    else:
        result = max(result)
    return result


@memorize
def get_column(column_index: int, matrix: list) -> list:
    result = []
    for row in matrix:
        result.append(row[column_index])

    return result


def test_left(column_index, row, row_index, cache):
    test_column_index = column_index - 1
    if test_column_index < 0:
        return 0

    counter = 0
    while test_column_index >= 0:
        if (row_index, test_column_index) in cache:
            counter += cache[(row_index, test_column_index)]
            return counter

        if row[test_column_index] == '1':
            counter += 1
            cache[(row_index, test_column_index)] = counter

        if row[test_column_index] == '0':
            return counter
        test_column_index -= 1
    return counter


def test_right(column_index, row, row_index, cache):
    test_column_index = column_index - 1
    counter = 0
    while test_column_index < len(row):

        if (row_index, test_column_index) in cache:
            counter += cache[(row_index, test_column_index)]
            return counter

        if row[test_column_index] == '1':
            counter += 1
            cache[(row_index, test_column_index)] = counter

        if row[test_column_index] == '0':
            return counter
        test_column_index += 1
    return counter


def test_bottom(row_index, column, column_index,cache):
    test_row_index = row_index + 1
    counter = 0
    while test_row_index < len(column):

        if (test_row_index, column_index) in cache:
            counter += cache[(test_row_index, column_index)]
            return counter

        if column[test_row_index] == '1':
            counter += 1
            cache[(test_row_index, column_index)] = counter

        if column[test_row_index] == '0':
            return counter

        test_row_index += 1
    return counter


def test_top(row_index, column, column_index, cache):
    test_row_index = row_index - 1
    if test_row_index < 0:
        return 0

    counter = 0
    while test_row_index >= 0:

        if (test_row_index, column_index) in cache:
            counter += cache[(test_row_index, column_index)]+1
            return counter

        if column[test_row_index] == '1':
            counter += 1
            cache[(test_row_index, column_index)] = counter

        if column[test_row_index] == '0':
            return counter

        test_row_index -= 1
    return counter


def getRelevantIndexes(matrix: list) -> set:
    result_set = set()
    row_index = 0
    for row in matrix:
        column_index = 0
        for column in row:
            if column == '1':
                result_set.add((row_index, column_index))
            column_index += 1
        row_index += 1
    return result_set


test_matrix = ["0000000",
 "0001000",
 "0001000",
 "0111110",
 "0001000",
 "0001000"]

print(biggestPlus(test_matrix))