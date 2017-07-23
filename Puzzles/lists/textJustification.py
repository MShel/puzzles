def textJustification(words, l):
    return_list = recursive_population(words, l)
    result_list = []
    ret_list_len = len(return_list)-1
    j = 0
    for char_amount, list_to_glue in return_list:
        list_to_glue_len = len(list_to_glue)
        if j == ret_list_len:
            last_line = ' '.join(list_to_glue)
            if len(last_line) <= l:
                spaces_to_add = l - len(last_line)
            result_list.append(last_line + ' ' * spaces_to_add)
            break
        if list_to_glue_len > 1:
            extra_spaces = (l - char_amount) % (list_to_glue_len - 1)
            repeat_n_times = int((l - char_amount) // (list_to_glue_len - 1))
            spaces = ' ' * repeat_n_times
            if extra_spaces == 0:
                result_list.append(spaces.join(list_to_glue))
            else:
                res = ''
                for i in range(len(list_to_glue) - 1):
                    res += list_to_glue[i] + spaces
                    if extra_spaces:
                        res += ' '
                        extra_spaces -= 1
                res += list_to_glue[i + 1]
                result_list.append(res)
        else:
            spaces = ' ' * (l - char_amount)
            result_list.append(list_to_glue.pop() + spaces)
        j += 1

    return result_list


def recursive_population(words, l, return_list=[]):
    words_to_add = []
    buffer_word = ''
    final_count = 0
    i = 0
    while len(buffer_word) <= l and words:
        buffer_word = ' '.join(words_to_add + [words[0]])
        if len(buffer_word) <= l:
            final_count = len(buffer_word) - len(words_to_add)
            popped_word = words.pop(0)
            words_to_add += [popped_word]
        else:
            break
        i += 1
    return_list.append((final_count, words_to_add))

    if words:
        recursive_population(words, l, return_list)

    return return_list


words = ["Looks",
 "like",
 "it",
 "can",
 "be",
 "a",
 "tricky",
 "test"]
l = 25

'''
["Looks  like  it  can be a", 
 "tricky test              "]
'''

print(textJustification(words, l))
