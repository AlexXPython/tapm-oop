# Определяем класс ProceduralLanguage для процедурных языков программирования
class ProceduralLanguage:
    def __init__(self, name, year, is_abstract_type_supported):
        self.name = name
        self.year = year
        self.is_abstract_type_supported = is_abstract_type_supported


# Определяем класс InheritanceType для типов наследования
class InheritanceType:
    Single = "Single"
    Multiple = "Multiple"


# Определяем класс ObjectOrientedLanguage для объектно-ориентированных языков программирования
class ObjectOrientedLanguage:
    def __init__(self, name, year, is_abstract_type_supported, inheritance_type, interfaces):
        self.name = name
        self.year = year
        self.is_abstract_type_supported = is_abstract_type_supported
        self.inheritance_type = inheritance_type
        self.interfaces = interfaces


# Создаем объекты процедурных языков программирования
c = ProceduralLanguage("C", 1972, False)
pascal = ProceduralLanguage("Pascal", 1970, True)
fortran = ProceduralLanguage("FORTRAN", 1957, False)
cobol = ProceduralLanguage("COBOL", 1959, False)
basic = ProceduralLanguage("BASIC", 1964, True)

# Создаем объекты объектно-ориентированных языков программирования
java = ObjectOrientedLanguage("Java", 1995, True, InheritanceType.Multiple, ["Java SE", "Java EE"])
cpp = ObjectOrientedLanguage("C++", 1983, True, InheritanceType.Multiple, ["STL", "Boost"])
python = ObjectOrientedLanguage("Python", 1991, True, InheritanceType.Multiple, ["ABC", "DEF"])
ruby = ObjectOrientedLanguage("Ruby", 1995, True, InheritanceType.Single, ["Ruby on Rails"])
swift = ObjectOrientedLanguage("Swift", 2014, True, InheritanceType.Multiple, ["UIKit", "Foundation"])

# Тестирование
print(c.name, c.year, c.is_abstract_type_supported)
print(java.name, java.year, java.is_abstract_type_supported, java.inheritance_type, java.interfaces)