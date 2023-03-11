from data_proc import fraction_str, complex_number_str, create_doubly_linked_list, doubly_linked_list_node_str, doubly_linked_list_append, doubly_linked_list_to_string
from typing import Union


def process_input(input_file, output_file):
    # Создаем пустой двунаправленный список
    linked_list = create_doubly_linked_list()

    # Читаем входной файл построчно
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            # Разделяем строку на список слов
            words = line.strip().split()
            # Если первое слово - "дробь", то добавляем новую дробь в список
            if words[0] == 'дробь':
                numerator = int(words[1])
                denominator = int(words[2])
                fraction = fraction_str(numerator, denominator)
                doubly_linked_list_append(linked_list, fraction)
            # Если первое слово - "комплексное", то добавляем новое комплексное число в список
            elif words[0] == 'комплексное':
                real = float(words[1])
                imag = float(words[2])
                complex_number = complex_number_str(real, imag)
                doubly_linked_list_append(linked_list, complex_number)

    # Записываем результаты в выходной файл
    with open(output_file, 'w') as fout:
        fout.write(doubly_linked_list_to_string(linked_list))