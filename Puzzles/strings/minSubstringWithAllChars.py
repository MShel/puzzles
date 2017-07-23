def minSubstringWithAllChars(s, t):
    all_lets = set(t)
    shortest = None
    for i in range(len(s)):
        found = set()
        j = i
        while found != all_lets:
            if j >= len(s):
                break
            if s[j] in all_lets:
                found.add(s[j])
            if found == all_lets:
                if not shortest or j-i+1 < len(shortest):
                    shortest = s[i:j+1]
            j += 1
    if not shortest:
        return ""
    return shortest

def minSubstringWithAllChars_1(s, t):
    t = set(t)
    if not t: return ""
    o = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            x = s[i:j]
            if t <= set(x): o.append(x); break
    if not o: return ""
    print(o)
    o.sort(key=len)
    return o[0]
#and (j - i < len(res))

test_set1 = set("abdabc")
test_set2 = set("abc")

print(test_set1.issuperset(test_set2))

print(minSubstringWithAllChars_1("abdabcobecodebancaflelf", "abc"))
