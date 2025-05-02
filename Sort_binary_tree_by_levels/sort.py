from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    result = []
    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return result
