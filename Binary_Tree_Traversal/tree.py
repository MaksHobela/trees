def pre_order(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    pre_order(node.left, result)
    pre_order(node.right, result)
    return result

def in_order(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    in_order(node.left, result)
    result.append(node.data)
    in_order(node.right, result)
    return result

def post_order(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    post_order(node.left, result)
    post_order(node.right, result)
    result.append(node.data)
    return result
