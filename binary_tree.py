tomorrowfrom fancy_tree_printer import print_fancy_tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def search(self, root, key):
        if root is None:
            return None
        if root.value == key:
            return root
        left_result = self.search(root.left, key)
        if left_result:
            return left_result
        return self.search(root.right, key)

    def delete_node(self, root, key):
        if root is None:
            return root
        if root.value == key:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            min_larger_node = self._find_min(root.right)
            root.value = min_larger_node.value
            root.right = self.delete_node(root.right, min_larger_node.value)
            return root
        if key < root.value:
            root.left = self.delete_node(root.left, key)
        else:
            root.right = self.delete_node(root.right, key)
        return root

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def display(self):
        return print_fancy_tree(self.root)

    def inorder(self, root):
        """In-order traversal (left, root, right)"""
        if root is None:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)


if __name__ == "__main__":
    # Initialize the binary tree
    tree = BinaryTree(10)
    tree.insert_left(tree.root, 5)
    tree.insert_right(tree.root, 15)
    tree.insert_left(tree.root.left, 2)
    tree.insert_right(tree.root.left, 7)
    tree.insert_left(tree.root.right, 12)
    tree.insert_right(tree.root.right, 20)

    # Print the tree
    print("Initial Tree:")
    print(tree.display())

    # In-order Traversal
    print("\nIn-order Traversal:", tree.inorder(tree.root))

    # Search for a value
    key_to_search = 7
    found_node = tree.search(tree.root, key_to_search)
    if found_node:
        print(f"Node with value {key_to_search} found.")
    else:
        print(f"Node with value {key_to_search} not found.")

    # Delete a node
    key_to_delete = 15
    tree.root = tree.delete_node(tree.root, key_to_delete)
    print(f"\nTree after deleting node {key_to_delete}:")
    print(tree.display())

    # In-order Traversal
    print("\nIn-order Traversal:", tree.inorder(tree.root))
