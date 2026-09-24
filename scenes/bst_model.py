from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> list[int]:
        if self.root is None:
            self.root = Node(value)
            return []

        path: list[int] = []
        current = self.root

        while True:
            path.append(current.value)

            if value == current.value:
                return path

            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return path
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return path
                current = current.right

    def search(self, value: int) -> tuple[list[int], bool]:
        path: list[int] = []
        current = self.root

        while current is not None:
            path.append(current.value)

            if value == current.value:
                return path, True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return path, False

    def inorder(self) -> list[int]:
        """Recorrido In-order."""
        values: list[int] = []
        self._inorder(self.root, values)
        return values

    def _inorder(self, node: Node | None, values: list[int]) -> None:
        if node is None:
            return

        self._inorder(node.left, values)
        values.append(node.value)
        self._inorder(node.right, values)
