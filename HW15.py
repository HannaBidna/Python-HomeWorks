def cyfra(a):
    if a.isdigit() is True:
        a = int(a)
        if a == 0:
           expl = ''
        else:
           expl = 'позитивне ціле'
    else:
        if a.startswith('-'):
            if a.lstrip().isdigit() is True and int(a.lstrip()) != 0:
               expl = 'негативне ціле'
            else:
                a = a.replace(',', '.')
                if a.split('.', 1)[0].strip('-').isdigit() is True and a.split('.', 1)[1].isdigit() is True:
                    expl = 'негативне дробове'
                else:
                    expl = 'не'
        else:
            a = a.replace(',', '.')
            parts = a.split('.', 1)
            if parts[0].isdigit() is True and parts[1].isdigit() is True:
                expl = 'позитивне дробове'
            else:
                expl = 'не'
    return (f'Ви ввели {expl} число: {a}')


def main():
    while True:
        print ('?')
        a = input()
        if a.upper() in ['ВИХІД', 'EXIT', 'QUIT', 'E', 'Q']:
            break
        else:
            #print(a)
            cyfra(a)
            print(cyfra(a))


main()
