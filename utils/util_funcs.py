from inspect import getmembers
from pprint import pprint

'''
we use prev_middle to keep track of proper index of original list
binary search is O - log N
'''
def binary_search(sorted_list, search_for, prev_middle=0):
    # that perhaps should go into separate function for parsing input
    try:
        middle = int(len(sorted_list) / 2)
        if len(sorted_list) < 2 and sorted_list[0] != search_for:
            return  -1;
    except TypeError:
        print('You need to provide type that is iterable')
        return

    if sorted_list[middle] == search_for:
        return prev_middle + middle
    elif sorted_list[middle] < search_for:
        prev_middle += middle
        return binary_search(array_slice(sorted_list, middle), search_for, prev_middle)
    else:
        return binary_search(array_slice(sorted_list, None, middle), search_for, prev_middle)


def quick_sort(list):
    pass


def traverse_tree(tree):
    pass


def search_tree(tree):
    pass


def remove_from_tree(tree):
    pass


def add_to_tree(tree):
    pass


def balanse_tree(tree):
    pass


def check_existance_of_key_in_dict(dict, key):
    return key in dict


def sort_list_of_dict(list, key_to_sort_by):
    return sorted(list, key=lambda k: k[key_to_sort_by])


def sort_dict_by_key(dict):
    sorted_dict = sorted(dict.items())
    return sorted_dict


'''
test array slice
[1, 4, 5, 6, 7, 8, 9, 11]
from 2 to 3
[5]
to 3
[1, 4, 5]
from 2
[5, 6, 7, 8, 9, 11]
'''
def array_slice(list, slice_from=None, slice_to=None):
    if slice_from and not slice_to:
        return_list = list[slice_from:]
        return return_list
    elif slice_to and not slice_from:
        return_list = list[:slice_to]
        return return_list
    elif slice_to and slice_from:
        if slice_from < slice_to:
            return_list = list[slice_from:]
            indext_to_cut_to = return_list.index(list[slice_to])
            return_list = return_list[:indext_to_cut_to]
            return return_list
    else:
        raise ValueError('invalid arguments provided')


def var_dump(var):
    pprint(getmembers(var))


'''
print(list(permutations_gen('abdc', '')))
'''
def permutations_gen(input, s):
    print(s)
    if len(s) == len(input):
        #print(s)
        yield s
    for i, v in enumerate(input):
        if v in s:
            continue
        s = s + v
        for x in permutations_gen(input, s):
            yield x
        s = s[:-1]


print(list(permutations_gen('abdc', '')))


def breadth_first_search(graph):
    pass


def depth_first_search(graph):
    pass
