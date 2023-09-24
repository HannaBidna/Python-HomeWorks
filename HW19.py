import csv
import json
import random

with open('test1.json') as f:
    new_test1 = json.load(f)

print(new_test1)

fields_name = ['id', 'Name', 'Age', 'Phone']
field1 = list(iter(new_test1))
field2 = list(item[0] for item in new_test1.values())
field3 = list(item[1] for item in new_test1.values())
list_code = ['095', '066', '098', '096', '050', '097']
field4 = list(str(random.choice(list_code)) + str(random.randrange(0000000, 9999999)) for i in range(len(field3)))

#print(field1, field2, field3, field4)

with open('test2.csv', 'w', encoding='UTF-8') as f:
    file_write = csv.writer(f, delimiter = ' ')
    for item in (fields_name, field1, field2, field3, field4):
        file_write.writerow(item)
