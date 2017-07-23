def reverseSentence(sentence):
    sentence_arr = sentence.split(' ')
    result =''
    while sentence_arr:
        word = sentence_arr.pop()
        if sentence_arr:
            result += word + ' '
        else:
            result += word
    return result

sentence = "Man bites dog"
print(reverseSentence(sentence))