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

    def get_from_file(self, file):
        self.title = file.readline()
        if self.language_type == LanguageType.PROCEDURAL:
            self.data_type = DataType(int(file.readline()))
        if self.language_type == LanguageType.OBJECT_ORIENTED:
            self.inheritance_type = InheritanceType(int(file.readline()))
        self.year = int(file.readline())

    def record_to_file(self, file):
        file.write(self.title)
        file.write(f"Год разработки: {self.year}\n")
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

def fill_array(file, max_size):
    a = []
    language_type = LanguageType(int(file.readline()))
    while language_type != '':
        lang = Lang(language_type)
        lang.get_from_file(file)
        a.append(lang)
        language_type_str = file.readline().strip()
        if not language_type_str:
            break
        language_type = LanguageType(int(language_type_str))
        # language_type = LanguageType(int(file.readline()))
        if len(a) >= max_size:
            break
    return a

def record_array_to_file(a, file):
    file.write(f"Записано {len(a)} язык(-а,-ов)\n\n")
    for lang in a:
        lang.record_to_file(file)

def main():
    if len(sys.argv) != 3:
        print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
        infile = 'in.txt'
        outfile = 'out.txt'
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]

    with open(infile, 'r', encoding="utf-8") as f_in, open(outfile, 'w', encoding = "utf-8") as f_out:
        a = fill_array(f_in, 2)
        print(f"В контейнер записано {len(a)} язык(-а,-ов)\n")
        record_array_to_file(a, f_out)

if __name__ == "__main__":
    main()