#2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
#"Один"
#>>> num_translate_adv("two")
#"два"


nums = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}
def num_translate_adv(eng_numerals):
    if eng_numerals[0].isupper():
        eng_numerals = eng_numerals.lower()
        print(nums[eng_numerals].title())
    else:
        print(nums[eng_numerals])
num_translate_adv('One')
#
#
def num_translate_adv(number):
    """
    Translates numerals from 0 to 10 from English to Russian.
    """
    dict_of_words = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
    }
    if number.istitle():
        number = number.lower()
        print(dict_of_words.get(number).title())
    else:
        print(dict_of_words.get(number))
num_translate_adv('Nine')
# num_translate_adv('six')
# num_translate_adv('восемь')