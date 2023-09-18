from datetime import datetime


def decor(x_func):
    def obkl():
        print(50 * '--')
        t_1 = datetime.now()
        x_func()
        t_2 = datetime.now()
        print('Time=',t_2-t_1)
        print(50 * '--')
    return obkl

@decor
def my_func():
    print('Будь-яка функція')

@decor
def cat_f():
    print('>^.^<')


my_func()

cat_f()