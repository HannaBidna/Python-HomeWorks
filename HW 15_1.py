def cyfra(a):
    if a.isdigit() is True:
        expl = 'позитивне ціле'
    elif a.lstrip('-').isdigit() is True:
        num = int(a.lstrip('-'))
        if num == 0:
           expl = ''
        elif num > 0:
           expl = 'негативне ціле'
        else:
            expl = 'не'

    else:
        try:
            a = a.replace(',', '.')
            num = float(a)
            if num > 0:
                expl = 'позитивне дробове'
            else:
                expl = 'негативне дробове'
        except ValueError:
             expl = 'не'
    return (f'Ви ввели {expl} число: {a}')


def main():
    while True:
        print ('?')
        a = input()
        if a.upper() in ['ВИХІД', 'EXIT', 'QUIT', 'E', 'Q']:
            break
        else:
            cyfra(a)
            print(cyfra(a))


main()
