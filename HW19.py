import csv
import json
import random

with open('test1.json') as f:
    new_test1 = json.load(f)

print(new_test1)

fields_name = ['id', 'Name', 'Age', 'Phone']

new_test1 = [[i, new_test1[i]] for i in new_test1]
print(new_test1)

list_code = ['095', '066', '098', '096', '050', '097']
phone = list(str(random.choice(list_code)) + str(random.randrange(0000000, 9999999)) for i in range(len(new_test1)))
print(phone)
field1 =[new_test1[0][0]] + [new_test1[0][1][j] for j in range(len(new_test1[0]))] + [phone[0]]
field2 = [new_test1[1][0]] + [new_test1[1][1][j] for j in range(len(new_test1[1]))] + [phone[1]]
field3 = [new_test1[2][0]] + [new_test1[2][1][j] for j in range(len(new_test1[2]))] + [phone[2]]
field4 = [new_test1[3][0]] + [new_test1[3][1][j] for j in range(len(new_test1[1]))] + [phone[3]]
field5 = [new_test1[4][0]] + [new_test1[4][1][j] for j in range(len(new_test1[4]))] + [phone[4]]
print(field1,field2, field3, field4, field5)





with open('test2.csv', 'w', encoding='UTF-8') as f:
    file_write = csv.writer(f, delimiter = ',')
    for item in (fields_name, field1, field2, field3, field4, field5):
        file_write.writerow(item)
