class Nodo:
    # Constructor
    def __init__(self, x=0):
        self.element = x
        self.left = None
        self.right = None
    # Getters and setters
    def set_element(self, element):
        self.element = element

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_element(self):
        return self.element

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def exists(self, x):
        if self.left is not None and self.left.element == x:
            return True
        if self.right is not None and self.right.element == x:
            return True
        return False

    def get_child(self, i):
        # Obtener el hijo i del nodo actual
        if i < 1 or i > 2:
            print("Nodo.get_child: {} no es un número de hijo correcto. Use 1 o 2.".format(i))
            return None
        return self.left if i == 1 else self.right

    def count_children(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def is_leaf(self):
        return self.count_children() == 0
