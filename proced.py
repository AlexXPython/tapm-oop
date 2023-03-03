# Процедурные языки программирования

procedural_languages = [
    {"name": "C", "year": 1972, "is_abstract_type_supported": False},
    {"name": "Pascal", "year": 1970, "is_abstract_type_supported": True},
    {"name": "FORTRAN", "year": 1957, "is_abstract_type_supported": False},
    {"name": "COBOL", "year": 1959, "is_abstract_type_supported": False},
    {"name": "BASIC", "year": 1964, "is_abstract_type_supported": True}
]


def find_procedural_language(name):
    for language in procedural_languages:
        if language["name"] == name:
            return language
    return None


# Объектно-ориентированные языки программирования

class ProgrammingLanguage:
    def __init__(self, name, year, is_abstract_type_supported, inheritance_type, interfaces):
        self.name = name
        self.year = year
        self.is_abstract_type_supported = is_abstract_type_supported
        self.inheritance_type = inheritance_type
        self.interfaces = interfaces


object_oriented_languages = [
    ProgrammingLanguage("Java", 1995, True, "Multiple", ["Java SE", "Java EE"]),
    ProgrammingLanguage("C++", 1983, True, "Multiple", ["STL", "Boost"]),
    ProgrammingLanguage("Python", 1991, True, "Multiple", ["ABC", "DEF"]),
    ProgrammingLanguage("Ruby", 1995, True, "Single", ["Ruby on Rails"]),
    ProgrammingLanguage("Swift", 2014, True, "Multiple", ["UIKit", "Foundation"])
]


def find_object_oriented_language(name):
    for language in object_oriented_languages:
        if language.name == name:
            return language
    return None

# Тестирование



print(find_procedural_language("C"))
print(find_procedural_language("BASIC"))

print(find_object_oriented_language("Python").name)
print(find_object_oriented_language("Java").year)
print(find_object_oriented_language("Swift").is_abstract_type_supported)
print(find_object_oriented_language("Ruby").inheritance_type)
print(find_object_oriented_language("C++").interfaces)