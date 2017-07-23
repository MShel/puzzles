from collections import deque

start_word = "hit"
end_word = "cog"
words_to_use = ["log", "hot", "dot", "dog", "lot", "cog"]


def wordLadder(beginWord, endWord, wordList):
    # use the whole alphabet not to depend on words to use
    alphabet = [chr(ord('a') + itr) for itr in range(26)]
    queue = deque([beginWord, None])
    level = 0
    while queue:
        print(queue)
        node = queue.popleft() #removing an item from the queue
        #if node is None but we got stuff in queue append the queue with None again and let code below process all the queue items until it gets to None again
        if not node:
            if not queue:
                break
            level += 1
            queue.append(None)
        else:
            if node == endWord:
                return level + 1
            for i in range(0, len(node)):
                for letter in alphabet:
                    if node[i] != letter:
                        # going through all possible combinations of word = node changing one letter at a time
                        word = node[:i] + letter + node[i + 1:]
                        if word in wordList:
                            print(word)
                            # append to the end of queue
                            queue.append(word)
                            # removing from the list
                            wordList.remove(word)
    return 0


print(wordLadder(start_word, end_word, words_to_use))
