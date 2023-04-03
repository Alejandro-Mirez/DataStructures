class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.path = []
        self.inorder_list = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(value, self.root)

    def insert_node(self, value, node):
        if value <= node.value:
            if node.left is not None:
                self.insert_node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self.insert_node(value, node.right)
            else:
                node.right = Node(value)

    def search(self, value):
        self.path = []
        self.inorder_traversal(self.root)
        if value in self.inorder_list:
            if value == self.root:
                result = self.path.append(self.root.value)
                print(result)
            else:
                self.path.append(self.root.value)
                self.search_node(value, self.root)
        else:
            raise ValueError("node does not exist in this tree")
        return self.path

    def search_node(self, value, node):
        if value == node.value:
            print(self.path)
        else:
            if value < node.value:
                self.path.append(node.left.value)
                self.search_node(value, node.left)
            else:
                self.path.append(node.right.value)
                self.search_node(value, node.right)
        return self.path


    def delete(self, value):
        if self.root is None:
            raise ValueError("Tree is empty, cannot delete")
        else:
            self.delete_node(value, self.root)

    def delete_node(self, value, node):
        self.inorder_traversal(self.root)
        if value in self.inorder_list:
            if value == node.value:
                node.value = None
                node.left = None
                node.right = None
            else:
                if value < node.value:
                    self.delete_node(value, node.left)
                else:
                    self.delete_node(value, node.right)
        else:
            raise ValueError("node does not exist in this tree, cannot delete")

    def inorder_traversal(self, node):
        self.inorder_list = []
        if node is not None:
            self.inorder_list = self.inorder_traversal(node.left)
            if node.value is not None:
                self.inorder_list.append(node.value)
            self.inorder_list = self.inorder_list + self.inorder_traversal(node.right)
        return self.inorder_list

