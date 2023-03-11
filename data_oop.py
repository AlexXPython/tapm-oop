from typing import Union
from abc import ABC, abstractmethod


class LinkedListNode(ABC):
    @abstractmethod
    def __str__(self):
        pass


class LinkedList(ABC):
    @abstractmethod
    def append(self, node: LinkedListNode):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Fraction(LinkedListNode):
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


class ComplexNumber(LinkedListNode):
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}{self.imag}i"
                # .replace("+", "+")


class DoublyLinkedListNode:
    def __init__(self, value: Union[Fraction, ComplexNumber], prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def append(self, node: DoublyLinkedListNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def __str__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return " -> ".join(values)