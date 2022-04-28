# # 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# # возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# # содержащие имена, начинающиеся с соответствующей буквы. Например:
# # >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# # {
# # "И": ["Иван", "Илья"],
# # "М": ["Мария"],
# # "П": ["Петр"]
# # }
# # Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
# # сортировка по ключам? Можно ли использовать словарь в этом случае?
#
# def thesaurus(*keys):
#     dict_names = {}
#     for key in keys:
#         dict_names.setdefault(key[0], [])
#         dict_names[key[0]].append(key)
#     return  dict_names
# print(thesaurus("Эмма", "Петр", "Саша", "Павел", "Bil", "Tim", "Tom"))

def thesaurus(*args):
    directory = {}
    for letter in args:
        directory[letter[0]] = directory.setdefault(letter[0], []) + [letter]
    directory = sorted(directory.items())
    print(dict(directory))
thesaurus('Вася', 'Петр', 'Игорь', 'Ирина', 'Абрам', 'Валера', 'Дмитрий', 'Полина', 'Света', 'Максим', 'Лео', 'Леонид', 'Люся')