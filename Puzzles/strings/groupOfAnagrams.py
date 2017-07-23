'''
O(N*log(n))
'''
def groupsOfAnagrams(words):
    invariants = ["".join(sorted(w)) for w in words]
    unique_invariants = set(invariants)
    return len(unique_invariants)


print(groupsOfAnagrams(["listen", "admirer", "tea", "eta", "eat", "ate", "silent", "tinsel", "enlist", "codefights", "married"]))