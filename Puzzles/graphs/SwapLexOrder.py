'''
Given a string str and array of pairs that indicates which indices in the string can be swapped, 
return the lexicographically largest string that results from doing the allowed swaps.
You can swap indices any number of times.
'''

# METHOD D: using sets
def groupsOfAnagrams(words):
    invariants = ["".join(sorted(w)) for w in words]
    unique_invariants = set(invariants)
    return len(unique_invariants)


print(groupsOfAnagrams(["listen", "admirer", "tea", "eta", "eat", "ate", "silent", "tinsel", "enlist", "codefights", "married"]))

def swapLexOrder_0(test_str, pairs):
    n = len(test_str)
    test_str_list = list(test_str)

    # generating list of sets to hold our swappable index of chars
    swaps = [set() for _ in range(n)]

    nodes = set()
    for a, b in pairs:
        swaps[a - 1].add(b - 1)
        swaps[b - 1].add(a - 1)
        nodes.add(a - 1)
        nodes.add(b - 1)

    while nodes:
        active = {nodes.pop()}
        group = set()
        while active:
            # |= returns sorted intersection of set
            # ex. {1,2} | {3,1} == {3,2,1} {3,4} |= {4,3} == {3,4}
            group |= active
            nodes -= active
            new_active = set()
            # that can be a generator
            for node in active:
                for index in swaps[node]:
                    if index in nodes:
                        new_active.add(index)
            active = new_active
        # getting generator for sorted chars high to low
        chars = iter(sorted((test_str_list[i] for i in group), reverse=True))
        for i in sorted(group):
            # only replacing chars that are in generator group
            test_str_list[i] = next(chars)
            print(test_str_list[i])

    return "".join(test_str_list)


def dfs(node, graph=[]):
    s = [node]
    d = []
    visited = set()
    while s:
        u = s.pop()
        if u in visited:
            continue
        visited.add(u)
        d.append(u)
        for v in graph[u]:
            s.append(v)
    d.sort()
    return d


'''
test = {3,4}
test|={4,3}
print(test)
'''

pairs = [[1, 4],
         [3, 4]]
test_str = "abdc"
print(swapLexOrder_0(test_str, pairs))
