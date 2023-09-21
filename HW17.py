str_1 = input()
str_2 = input()
str_3 = input()
str_4 = input()

f1 = open('file1.txt', 'w')
f1.write(f'{str_1}\n{str_2}')
f1.close()

with open('file1.txt', 'a') as f1:
    f1.write(f'\n{str_3}\n{str_4}')

try:
    f = open('file1.txt')
    new_file = f.readlines()
finally:
    f.close()

for item in new_file:
    print(item.strip('\n'))
