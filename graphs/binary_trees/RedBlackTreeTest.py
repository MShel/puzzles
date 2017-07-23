from RedBlackBinaryTree import rbtree
import random

def test_tree(t, keys):
    "Insert keys one by one checking invariants and membership as we go."
    assert t.check_invariants()
    for i, key in enumerate(keys):
        for key2 in keys[:i]:
            assert t.nil != t.search(key2)
        for key2 in keys[i:]:
            assert (t.nil == t.search(key2)) ^ (key2 in keys[:i])
        t.insert_key(key)
        assert t.check_invariants()

size = 100
keys = random.sample(xrange(size), size)
t = rbtree()
for k in keys:
    t.insert_key(k)

print(vars(t.search(11, t.root)))