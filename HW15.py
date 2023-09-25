def cyfra(a):
    if a.isdigit() is True:
        a = int(a)
        if a == 0:
           expl = ''
        else:
           expl = 'позитивне ціле'
    else:
        if a.startswith('-'):
            if a[1:len(a)].isdigit() is True and int(a[1:len(a)]) != 0:
               expl = 'негативне ціле'
               a = int(a.lstrip())
            else:
                a = a.replace(',', '.')
                b = a.split('.', 1)
                print(b)
                if b[0].strip('-').isdigit() is True and b[1].isdigit() is True:
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
