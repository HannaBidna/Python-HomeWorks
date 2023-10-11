def geom_progres(first, step):
    i = 1
    while True:
        result = first * (step ** (i-1))
        i = i + 1
        yield result


get_progres_1 = geom_progres(-2, -5)
print(next(get_progres_1))
print(next(get_progres_1))
print(next(get_progres_1))
print(next(get_progres_1))
print(next(get_progres_1))
print(next(get_progres_1))
print('-'*100)
get_progres_2 = geom_progres(10, 3)
print(next(get_progres_2))
print(next(get_progres_2))
print(next(get_progres_2))
print(next(get_progres_2))
print(next(get_progres_2))
print(next(get_progres_2))