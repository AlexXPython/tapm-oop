from data_oop import Fraction, ComplexNumber, DoublyLinkedList, DoublyLinkedListNode
from typing import Union


def process_input(input_file, output_file):
    # Создаем пустой двунаправленный список
    linked_list = DoublyLinkedList()

    # Читаем входной файл построчно
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            # Разделяем строку на список слов
            words = line.strip().split()
            # Если первое слово - "дробь", то добавляем новую дробь в список
            if words[0] == 'дробь':
                numerator = int(words[1])
                denominator = int(words[2])
                fraction = Fraction(numerator, denominator)
                node = DoublyLinkedListNode(fraction)
                linked_list.append(node)
            # Если первое слово - "комплексное", то добавляем новое комплексное число в список
            elif words[0] == 'комплексное':
                real = float(words[1])
                imag = float(words[2])
                complex_number = ComplexNumber(real, imag)
                node = DoublyLinkedListNode(complex_number)
                linked_list.append(node)

    # Записываем результаты в выходной файл
    with open(output_file, 'w') as fout:
        for item in linked_list:
            fout.write(str(item) + '\n')
