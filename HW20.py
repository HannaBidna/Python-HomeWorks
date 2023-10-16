import csv
import openpyxl


with open('test3.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    r = []
    for item in reader:
        r = r + [item]

wb = openpyxl.Workbook()
sh = wb.create_sheet('First', index=0)



sh.delete_cols(3, 1)
wb.save('test4.xlsx')
