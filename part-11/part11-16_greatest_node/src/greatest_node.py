class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    if root is None:
        return float('-inf')
    
    greatest = root.value
    node_greatest_left = greatest_node(root.left_child)
    node_greatest_right = greatest_node(root.right_child)

    greatest = max(greatest, node_greatest_left, node_greatest_right)

    return(greatest)

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))
