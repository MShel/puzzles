def inorderTraversal(self, root):
    # write your code here
    if root is None:
        return []
    inorder = []
    self.rec(root, inorder)
    return inorder


def rec(self, node, order):
    if node.left:
        self.rec(node.left, order)
    order.append(node.val)
    if node.right:
        self.rec(node.right, order)


