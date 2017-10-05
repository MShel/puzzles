import copy 
def mergeTwoLinkedLists(node_a, node_b):
    if not node_a:
        return node_b
    if not node_b:
        return node_a
    
    start_node, end_node = (node_a, node_b) if node_a.value <= node_b.value else (node_b, node_a)  
    to_return = start_node
    
    while start_node.next is not None and end_node is not None:
        if start_node.next.value <= end_node.value:
            start_node = start_node.next
        else:
            temp_node = copy.copy(start_node.next)
            while end_node is not None and end_node.value < temp_node.value:
                start_node.next = end_node
                start_node = start_node.next
                end_node = end_node.next
            start_node.next = temp_node
            start_node = start_node.next
    
    if end_node is not None:
        start_node.next = end_node
        
    return to_return
