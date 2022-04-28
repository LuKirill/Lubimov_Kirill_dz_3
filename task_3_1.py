# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

# удобней использовать словать, тк запись получается короче
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
def num_translate(numerals):
    a = input("Введите число: ")
    print(nums.get(a))
num_translate(nums)

#или
# num = input("num_translate: ")
# if num == "zero":
#     print("ноль")
# elif num == "one":
#     print("один")
# elif num == "two":
#     print("два")
# elif num == "three":
#     print("три")
# elif num == "four":
#     print("четыре")
# elif num == "five":
#     print("пять")
# elif num == "six":
#     print("шесть")
# elif num == "seven":
#     print("семь")
# elif num == "eight":
#     print("восемь")
# elif num == "nine":
#     print("девять")
# elif num == "ten":
#     print("десять")