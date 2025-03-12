import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return ", ".join(elements)


def main():
    linked_list = LinkedList()


    for _ in range(10):
        zahl = random.randint(0, 100)
        linked_list.append(zahl)

    print("Inhalt der Liste:")
    print(linked_list)

    print("Iterative Ausgabe der Liste:")
    for value in linked_list:
        print(value, end=" -> ")
    print("None")

    print("Länge der Liste:", len(linked_list))

if __name__ == '__main__':
    main()
