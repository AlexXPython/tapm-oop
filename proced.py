import sys
from enum import Enum


class LanguageType(Enum):
    PROCEDURAL = 1
    OBJECT_ORIENTED = 2


class DataType(Enum):
    BOOLEAN = 11
    ABSTRACT = 22


class InheritanceType(Enum):
    SINGLE = 1
    MULTIPLE = 2


class Lang:
    def __init__(self, language_type):
        self.title = ''
        self.language_type = language_type
        self.data_type = None
        self.inheritance_type = None
        self.year = None
        self.next = None
        self.prev = None

    def get_from_file(self, file):
        self.title = file.readline()
        if self.language_type == LanguageType.PROCEDURAL:
            self.data_type = DataType(int(file.readline()))
        if self.language_type == LanguageType.OBJECT_ORIENTED:
            self.inheritance_type = InheritanceType(int(file.readline()))
        self.year = int(file.readline())

    def record_to_file(self, file):
        file.write(self.title)
        file.write(f"Год: {self.year}\n")
        if self.language_type == LanguageType.PROCEDURAL:
            file.write("Процедурный язык программирования\n")
            if self.data_type == DataType.BOOLEAN:
                file.write("Булевая величина\n")
            if self.data_type == DataType.ABSTRACT:
                file.write("Абстрактные типы данных отсутствуют\n")
        if self.language_type == LanguageType.OBJECT_ORIENTED:
            file.write("Объектно-ориентированный язык программирования\n")
            if self.inheritance_type == InheritanceType.SINGLE:
                file.write("Одинарное наследование\n")
            if self.inheritance_type == InheritanceType.MULTIPLE:
                file.write("Множественное наследование\n")
            file.write("Интерфейсы: есть\n")
        file.write('\n')


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, element):
        if self.head is None:
            self.head = element
            self.tail = element
        else:
            element.prev = self.tail
            self.tail.next = element
            self.tail = element
        self.size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def fill(self, file):
        language_type = int(file.readline())
        while language_type:
            lang = Lang(LanguageType(language_type))
            lang.get_from_file(file)
            self.append(lang)
            language_type_str = file.readline().strip()
            if not language_type_str:
                break
            language_type = int(language_type_str)

    def record_to_file(self, file):
        file.write(f"Записано {self.size} языков\n\n")
        cur = self.head
        while cur:
            cur.record_to_file(file)
            cur = cur.next


if len(sys.argv) != 3:
    print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
    infile = 'in.txt'
    outfile = 'out.txt'
else:
    infile = sys.argv[1]
    outfile = sys.argv[2]

infile = open(infile, 'r', encoding="utf-8")
a = LinkedList()
a.fill(infile)
print(f"В контейнер записано {a.size} языков\n")
infile.close()

outfile = open(outfile, 'w', encoding="utf-8")
outfile.write(f"В контейнер записано {len(a)} язык(-а,-ов)\n")
a.record_to_file(outfile)
outfile.close()
a.clear()