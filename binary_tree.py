from fancy_tree_printer import print_fancy_tree


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