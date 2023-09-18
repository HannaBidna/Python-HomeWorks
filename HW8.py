import random


def more_num():
    print('Наше число більше ;) Спробуй ще!')
    print(50 * '-')


def less_num():
    print('Наше число менше ;) Спробуй ще!')
    print(50 * '-')


def vanga():
    print('Да ти Ванга! Вгадано!')


def sproba(i):
    print('Спроба №%s. Введіть число від 1 до 10:' % (i))


answer = ''
while True:
    num_1 = random.randint(1, 10)
    #print(num_1)
    print('Ми загадали ціле число від  1 до  10 :)\nУ тебе є 3 спроби вгадати, яке саме ;)')
    print(50 * '-')

    i=1
    while i<4:
         sproba(i)
         attemp = int(input())
         i = i + 1
         if attemp < num_1:
            more_num()
         elif attemp > num_1:
            less_num()
         else:
            vanga()
            break

    print('Пограємо ще? (Так)')
    answer =input().upper()
    if answer != 'ТАК':
       break








