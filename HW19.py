import csv
import json
import random

with open('test1.json') as f:
    new_test1 = json.load(f)
fields_name = ['id', 'Name', 'Age', 'Phone']
new_test1 = [[i, new_test1[i]] for i in new_test1]
list_code = ['095', '066', '098', '096', '050', '097']
phone = list(str(random.choice(list_code)) + str(random.randrange(0000000, 9999999)) for i in range(len(new_test1)))

with open('test3.csv', 'w', encoding='UTF-8') as f:
    file_write = csv.writer(f, delimiter=',')
    file_write.writerow(fields_name)

for i in range(len(new_test1)):
    field = [new_test1[i][0]] + [new_test1[i][1][j] for j in range(len(new_test1[i]))] + [(phone[i])]
    with open('test3.csv', 'a', encoding='UTF-8') as f:
        file_write = csv.writer(f, delimiter=',')
        file_write.writerow(field)
    i = i + 1







