# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "теплый"]

def get_joke(nums):
    """Get random list from nouns, adverbs, adjectives"""
    jokes = []
    for num in range(nums):
        first = choice(nouns)
        second = choice(adverbs)
        third = choice(adjectives)
        jokes.append(f'{first}, {second}, {third}')
    print(jokes)
get_joke(2)

from random import shuffle
def get_jokes_adv(num, repeats=True): # включаем условие повторы разрешены
    joke_list = []

    if not repeats: # условия для неповторяющихся слов
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            print("no way")
        else:
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            for i in range(num):
                joke_list.append(f'{nouns[i]}, {adverbs[i]}, {adjectives[i]}')
    print(joke_list)
get_jokes_adv(2, False)
