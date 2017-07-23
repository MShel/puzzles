# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    check_list = []
    while l:
        check_list.append(l.value)
        l = l.next

    return isPalindrome(check_list)

def isPalindrome(n_list):
  for i in range(0, int(len(n_list)/2)):
    if n_list[i] != n_list[-(i+1)]:
        return False
  return True


def isListPalindrome(l):
    s = []
    while l != None:
        s.append(l.value)
        l = l.next
    return s == s[::-1]


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    count = 0
    prev = None
    node = l
    stack = []

    while node is not None:
        prev = node
        node = node.next
        count += 1

    node = l
    index = 0
    while node is not None and index < count // 2:
        stack.append(node.value)
        node = node.next
        index += 1

    if count % 2 == 1:
        node = node.next

    while node is not None and stack:
        if stack.pop() == node.value:
            node = node.next
        else:
            return False
    return True


test = [1,2,3,4,5,6]
print(test[::-1])