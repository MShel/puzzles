from collections import deque

def countClouds(skyMap):
    if len(skyMap) == 0:
        return 0
    cloud_list = get_cloud_list(skyMap)
    if not cloud_list:
        return 0

    column_len = len(skyMap[0])
    row_len = len(skyMap)

    if len(cloud_list) == 1 and cloud_list[0][0] == column_len - 1 and cloud_list[0][1] == row_len - 1:
        return 1

    vizited_dictionary = {}
    number_of_clouds = 0
    for cloud in cloud_list:
        if cloud in vizited_dictionary:
            continue
        else:
            number_of_clouds += 1
            vizited_dictionary = run_bfs(cloud, vizited_dictionary, row_len, column_len, skyMap)
    return number_of_clouds


def run_bfs(first_cloud: tuple, vizited_dictionary: dict, row_len: int, column_len: int, skyMap):
    queue = deque([first_cloud])
    while queue:
        cloud_column, cloud_row = queue.pop()
        vizited_dictionary[(cloud_column, cloud_row)] = True
        if not (cloud_column, cloud_row+1) in vizited_dictionary and cloud_row + 1 < row_len and skyMap[cloud_row + 1][cloud_column] == '1':
            queue.append((cloud_column, cloud_row + 1))
            vizited_dictionary[(cloud_column, cloud_row + 1)] = True

        if not (cloud_column, cloud_row-1) in vizited_dictionary and cloud_row - 1 >= 0 and skyMap[cloud_row - 1][cloud_column] == '1':
            queue.append((cloud_column, cloud_row - 1))
            vizited_dictionary[(cloud_column, cloud_row - 1)] = True

        if not (cloud_column+1, cloud_row) in vizited_dictionary and cloud_column + 1 < column_len and skyMap[cloud_row][cloud_column + 1] == '1':
                queue.append((cloud_column + 1, cloud_row))
                vizited_dictionary[(cloud_column + 1, cloud_row)] = True

        if not (cloud_column-1, cloud_row) in vizited_dictionary and cloud_column - 1 >= 0 and skyMap[cloud_row][cloud_column - 1] == '1':
            queue.append((cloud_column - 1, cloud_row))
            vizited_dictionary[(cloud_column - 1, cloud_row)] = True

    return vizited_dictionary

def get_cloud_list(sky_map: list) -> tuple:
    cloud_value = "1"
    cloud_collection = []
    row_index = 0
    column_index = 0
    for row in sky_map:
        column_index = 0
        for column in row:
            if column == cloud_value:
                # we only care about clouds yo check there neighbors
                # for 1's
                cloud_collection.append((int(column_index), int(row_index)))
            column_index += 1
        row_index += 1

    if cloud_collection:
        return cloud_collection
    return 0


skyMap = [["0", "1", "1", "0", "1"],
          ["0", "1", "1", "1", "1"],
          ["0", "0", "0", "0", "1"],
          ["1", "0", "0", "1", "1"]]

skyMap = [["1","1","1","1","1","1","1"]]
print(countClouds(skyMap))

