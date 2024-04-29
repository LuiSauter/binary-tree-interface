from nodo import Nodo
class Tree:
    """
    Clase que representa un árbol binario
    """
    """Crea una instancia de la clase Árbol Binario"""
    __raiz__ = None
    __n__ = 0

    def __init__(self):
        """Inicializa la raíz del árbol"""
        self.__raiz__ = None
        self.__n__ = 0

    def insert_recursive(self, element: int):
        """Método para insertar un elemento en el árbol de manera iterativa"""
        if self.search(element):
            return
        if self.empty():
            self.__raiz__ = Nodo(element)
        else:
            self.__insert_recursive(element, self.__raiz__)

    def __insert_recursive(self, element: int, current_node: Nodo):
        """Método para insertar un elemento en el árbol de manera iterativa"""
        if element < current_node.element:
            if current_node.left is None:
                current_node.left = Nodo(element)
            else:
                self.__insert_recursive(element, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Nodo(element)
            else:
                self.__insert_recursive(element, current_node.right)

    def insert_iterative(self, element: int):
        """Método para insertar un elemento en el árbol de manera iterativa"""
        # si el nodo ya existe, se retorna
        if self.search(element):
            return
        if self.empty():
            self.__raiz__ = Nodo(element)
        else:
            self.__insert_iterative(element, self.__raiz__)

    def __insert_iterative(self, element: int, current_node: Nodo):
        """Método auxiliar para insertar un elemento en el árbol de manera iterativa"""
        if self.empty():
            self.__raiz__ = Nodo(element)
        else:
            current_node = self.__raiz__
            while current_node:
                if element < current_node.element:
                    if current_node.left is None:
                        current_node.left = Nodo(element)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Nodo(element)
                        break
                    else:
                        current_node = current_node.right

    def search(self, value: int):
        """Método para buscar un elemento en el árbol"""
        return self.__search(self.__raiz__, value)

    def __search(self, current_node: Nodo, value: int):
        if current_node is None:
            return None
        elif current_node.element == value:
            return current_node
        elif value < current_node.element:
            return self.__search(current_node.left, value)
        else:
            return self.__search(current_node.right, value)

    def pre_order_recursive(self):
        """Método para recorrer el árbol en pre orden de manera recursiva"""
        # pre order: raíz, izquierda, derecha
        pila =  []
        self.__pre_order_recursive(self.__raiz__, pila)
        return pila

    def __pre_order_recursive(self, current_node: Nodo, pila: list):
        """Se recorre primero la raíz, luego el subárbol izquierdo y finalmente el subárbol derecho"""
        if current_node is None:
            return
        pila.append(current_node.element)
        self.__pre_order_recursive(current_node.left, pila)
        self.__pre_order_recursive(current_node.right, pila)

    def pre_order_iterative(self):
        """Método para recorrer el árbol en pre orden de manera iterativa."""
        # pre order: raíz, izquierda, derecha
        pila = []
        stack = []
        stack.append(self.__raiz__)
        while stack:
            current_node: Nodo = stack.pop()
            pila.append(current_node.element)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return pila

    def in_order_recursive(self):
        """Método para recorrer el árbol en in orden de manera recursiva"""
        pila = []
        self.__in_order_recursive(self.__raiz__, pila)
        return pila

    def __in_order_recursive(self, current_node: Nodo, pila: list):
        """Se recorre primero el subárbol izquierdo, luego la raíz y finalmente el subárbol derecho"""
        if current_node is None:
            return
        self.__in_order_recursive(current_node.left, pila)
        pila.append(current_node.element)
        self.__in_order_recursive(current_node.right, pila)

    def in_order_iterative(self):
        """
        Método para recorrer el árbol en in orden de manera iterativa.
        """
        # in order: izquierda, raíz, derecha
        pila = []
        stack = []
        current_node = self.__raiz__
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            pila.append(current_node.element)
            current_node = current_node.right
        return pila

    def post_order_recursive(self):
        """Método para recorrer el árbol en post orden de manera recursiva."""
        pila = []
        self.__post_order_recursive(self.__raiz__, pila)
        return pila

    def __post_order_recursive(self, current_node, pila):
        """Se recorre primero el subárbol izquierdo, luego el subárbol derecho y finalmente la raíz"""
        if current_node is None:
            return
        self.__post_order_recursive(current_node.left, pila)
        self.__post_order_recursive(current_node.right, pila)
        pila.append(current_node.element)

    def post_order_iterative(self):
        """Método para recorrer el árbol en post orden de manera iterativa."""
        # post order: izquierda, derecha, raízs
        pila = []
        stack = []
        current_node = self.__raiz__
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                pila.insert(0, current_node.element)
                current_node = current_node.right
            current_node = stack.pop()
            current_node = current_node.left
        return pila

    def search_iterative(self, value: int):
        """Método para buscar un elemento en el árbol de manera iterativa"""
        current_node = self.__raiz__
        while current_node:
            if current_node.element == value:
                return current_node
            if value < current_node.element:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def search_recursive(self, value: int):
        """Método para buscar un elemento en el árbol de manera recursiva"""
        return self.__search_recursive(self.__raiz__, value)

    def __search_recursive(self, current_node: Nodo, value: int):
        """Método auxiliar para buscar un elemento en el árbol de manera recursiva"""
        if current_node is None:
            return None
        if current_node.element == value:
            return current_node
        if value < current_node.element:
            return self.__search_recursive(current_node.left, value)
        return self.__search_recursive(current_node.right, value)

    def delete_recursive(self, value: int):
        """Método para eliminar un elemento del árbol de manera recursiva"""
        self.__raiz__ = self.__delete_recursive(self.__raiz__, value)

    def __delete_recursive(self, current_node: Nodo, value: int):
        """Método auxiliar para eliminar un elemento del árbol de manera recursiva"""
        if current_node is None:
            return None
        if value < current_node.element:
            current_node.left = self.__delete_recursive(current_node.left, value)
        elif value > current_node.element:
            current_node.right = self.__delete_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            if current_node.right is None:
                return current_node.left
            current_node.element = self.__min_value(current_node.right)
            current_node.right = self.__delete_recursive(current_node.right, current_node.element)
        return current_node

    def delete_iterative(self, value: int):
        """Método para eliminar un elemento del árbol de manera iterativa"""
        current_node = self.__raiz__
        parent = None
        while current_node:
            if value < current_node.element:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.element:
                parent = current_node
                current_node = current_node.right
            else:
                if current_node.left is None:
                    if parent is None:
                        self.__raiz__ = current_node.right
                    elif parent.left == current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    current_node = None
                elif current_node.right is None:
                    if parent is None:
                        self.__raiz__ = current_node.left
                    elif parent.left == current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    current_node = None
                else:
                    current_node.element = self.__min_value(current_node.right)
                    parent = current_node
                    current_node = current_node.right

    def __min_value(self, current_node: Nodo):
        """Método para obtener el valor mínimo de un subárbol"""
        while current_node.left:
            current_node = current_node.left
        return current_node.element

    def delete_sucesor(self, nodo: Nodo, value: int):
        """Método para eliminar un elemento del árbol usando el sucesor"""
        # Inicializa el nodo padre y el nodo actual
        father = None
        current_nodo = nodo

        # Busca el nodo con el valor especificado
        while current_nodo is not None and current_nodo.element != value:
            father = current_nodo
            current_nodo = current_nodo.left if value < current_nodo.element else current_nodo.right

        # Si no se encuentra el nodo, retorna el subárbol derecho
        if current_nodo is None:
            return nodo.right
        # Si el nodo padre es None, actualiza el hijo izquierdo del nodo
        elif father is None:
            nodo.set_left(current_nodo.right)
        else:
            father.set_left(current_nodo.right)
        return nodo

    def balance_recursive(self):
        """Equilibra el árbol binario recursivamente."""
        self.__raiz__ = self.__balance_recursive(self.__raiz__)

    def __balance_recursive(self, nodo: Nodo):
        """Equilibra el subárbol recursivamente."""
        if nodo is None:
            return None

        # Balancea recursivamente los subárboles izquierdo y derecho
        nodo.set_left(self.__balance_recursive(nodo.left))
        nodo.set_right(self.__balance_recursive(nodo.right))

        # Calcula el factor de equilibrio del nodo actual
        balance_factor = self.calculate_balance_factor(nodo)

        # Realiza rotaciones según el factor de equilibrio
        if balance_factor > 1:
            if self.calculate_balance_factor(nodo.left) < 0:
                nodo.set_left(self.rotate_left(nodo.left))
            return self.rotate_right(nodo)
        elif balance_factor < -1:
            if self.calculate_balance_factor(nodo.right) > 0:
                nodo.set_right(self.rotate_right(nodo.right))
            return self.rotate_left(nodo)
        # Si no se necesita balancear, retorna el nodo sin cambios
        return nodo

    def calculate_balance_factor(self, nodo: Nodo):
        """Calcula el factor de equilibrio de un nodo dado."""
        # Calcula la altura del subárbol izquierdo y derecho
        altura_izq = self.calculate_height(nodo.left)
        altura_der = self.calculate_height(nodo.right)

        # Retorna el factor de equilibrio (diferencia de alturas)
        return altura_izq - altura_der

    def calculate_height(self, node: Nodo):
        """Calcule la altura de un subárbol a partir de un nodo determinado."""
        # Si el nodo es None, la altura es 0
        if node is None:
            return 0

        # Calcula la altura de los subárboles izquierdo y derecho
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        # Retorna la altura máxima más uno
        return max(left_height, right_height) + 1

    def rotate_right(self, node: Nodo):
        """Realice una rotación hacia la derecha en un nodo determinado para equilibrar el árbol."""
        # El nuevo nodo raíz será el hijo izquierdo del nodo dado
        new_root: Nodo = node.left

        # El hijo derecho del hijo izquierdo del nodo dado será el hijo izquierdo del nodo dado
        node.set_left(new_root.right)

        # El nodo dado se convierte en el hijo derecho del nuevo nodo raíz
        new_root.set_right(node)

        return new_root

    def rotate_left(self, node: Nodo):
        """Realice una rotación hacia la izquierda en un nodo determinado para equilibrar el árbol."""
        # El nuevo nodo raíz será el hijo derecho del nodo dado
        new_root: Nodo = node.right

        # El hijo izquierdo del hijo derecho del nodo dado será el hijo derecho del nodo dado
        node.set_right(new_root.left)

        # El nodo dado se convierte en el hijo izquierdo del nuevo nodo raíz
        new_root.set_left(node)

        return new_root

    def empty(self):
        """Método para verificar si el árbol está vacío"""
        return self.__raiz__ is None

    def show(self, pila):
        """Método para mostrar el árbol"""
        print(' '.join(map(str, pila)))

    def is_leaf(self, nodo: Nodo):
        """Método para verificar si un nodo es hoja"""
        return nodo.left is None and nodo.right is None

    def height(self):
        """Método para obtener la altura del árbol"""
        return self.__height(self.__raiz__)

    def __height(self, current_node):
        # Primero se obtiene la altura del subárbol izquierdo y luego la altura del subárbol derecho. Se retorna la altura máxima más uno
        if current_node is None:
            return 0
        return max(self.__height(current_node.left), self.__height(current_node.right)) + 1

    def amount(self):
        """Método para obtener la cantidad de nodos en el árbol"""
        return self.__amount(self.__raiz__)

    def __amount(self, current_node):
        # Se obtiene la cantidad de nodos en el subárbol izquierdo, luego la cantidad de nodos en el subárbol derecho y finalmente se retorna la cantidad de nodos más uno
        if current_node is None:
            return 0
        return self.__amount(current_node.left) + self.__amount(current_node.right) + 1

    def amplitude(self):
        """Método para obtener la amplitud del árbol"""
        return self.amount() if self.__raiz__ else 0

def main():
    tree = Tree()
    tree.insert_iterative(10)
    tree.insert_iterative(5)
    tree.insert_iterative(15)
    tree.insert_iterative(3)
    tree.insert_iterative(7)
    tree.insert_iterative(12)
    tree.insert_iterative(17)
    print("Recorrido en pre orden de manera recursiva")
    tree.show(tree.pre_order_recursive())
    print("Recorrido en pre orden de manera iterativa")
    tree.show(tree.pre_order_iterative())
    print("Recorrido en in orden de manera recursiva")
    tree.show(tree.in_order_recursive())
    print("Recorrido en in orden de manera iterativa")
    tree.show(tree.in_order_iterative())
    print("Recorrido en post orden de manera recursiva")
    tree.show(tree.post_order_recursive())
    print("Recorrido en post orden de manera iterativa")
    tree.show(tree.post_order_iterative())
    print("Altura del árbol")
    print(tree.height())
    print("Cantidad de nodos en el árbol")
    print(tree.amount())
    print("Amplitud del árbol")
    print(tree.amplitude())

if __name__ == "__main__":
    main()