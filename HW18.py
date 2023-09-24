import json

data1 = {
     111111: ('Shevchenko', 34),
     111112: ('Franko', 45),
     111113: ('Stus', 23),
     111114: ('Symonenko', 66),
     111115: ('Kostenko', 33)

}


with open('test1.json', 'w') as f:
    json.dump(data1, f)

