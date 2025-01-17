class AVLNode:
    def __init__(self, order_id, details):
        self.order_id = order_id
        self.details = details
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, order_id, details):
        if not node:
            return AVLNode(order_id, details)

        if order_id < node.order_id:
            node.left = self.insert(node.left, order_id, details)
        elif order_id > node.order_id:
            node.right = self.insert(node.right, order_id, details)
        else:
            return node  

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and order_id < node.left.order_id:
            return self.rotate_right(node)
        if balance < -1 and order_id > node.right.order_id:
            return self.rotate_left(node)
        if balance > 1 and order_id > node.left.order_id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and order_id < node.right.order_id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, node, order_id):
        if not node:
            return node

        if order_id < node.order_id:
            node.left = self.delete(node.left, order_id)
        elif order_id > node.order_id:
            node.right = self.delete(node.right, order_id)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_min_value_node(node.right)
            node.order_id = temp.order_id
            node.details = temp.details
            node.right = self.delete(node.right, temp.order_id)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def preorder(self, node):
        if not node:
            return
        print(f"Order ID: {node.order_id}, Details: {node.details}")
        self.preorder(node.left)
        self.preorder(node.right)


if __name__ == "__main__":
    tree = AVLTree()
    root = None
    root = tree.insert(root, 101, "1x Pizza")
    root = tree.insert(root, 102, "2x Burgers")
    root = tree.insert(root, 103, "1x Pasta")
    root = tree.insert(root, 100, "1x Salad")
    print("Orders in AVL Tree (Preorder Traversal):")
    tree.preorder(root)
    print("\nDeleting order with ID 102...")
    root = tree.delete(root, 102)
    print("Updated Orders in AVL Tree (Preorder Traversal):")
    tree.preorder(root)
