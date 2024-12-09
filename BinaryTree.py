class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, id, name, price):
        new_product = Product(id, name, price)
        if self.root is None:
            self.root = new_product
        else:
            self._insert_recursive(self.root, new_product)

    def _insert_recursive(self, current, new_product):
        if new_product.id < current.id:
            if current.left is None:
                current.left = new_product
            else:
                self._insert_recursive(current.left, new_product)
        else:
            if current.right is None:
                current.right = new_product
            else:
                self._insert_recursive(current.right, new_product)

    def search(self, id):
        return self._search_recursive(self.root, id)

    def _search_recursive(self, current, id):
        if current is None or current.id == id:
            return current
        if id < current.id:
            return self._search_recursive(current.left, id)
        return self._search_recursive(current.right, id)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f'ID: {node.id}, Name: {node.name}, Price: {node.price}')
            self.inorder_traversal(node.right)

# Fungsi utama untuk menjalankan program
def main():
    bst = BST()
    
    # Menambahkan produk
    bst.insert(1, "Produk A", 10000)
    bst.insert(2, "Produk B", 20000)
    bst.insert(3, "Produk C", 15000)

    print("Inorder Traversal of Products:")
    bst.inorder_traversal(bst.root)

    # Mencari produk
    product_id = 2
    product = bst.search(product_id)
    if product:
        print(f'Found Product: ID: {product.id}, Name: {product.name}, Price: {product.price}')
    else:
        print("Product not found.")

if __name__ == "__main__":
    main()