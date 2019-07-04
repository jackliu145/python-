import csv

with open('dict.csv', 'w') as f:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerow({'id':'1', 'name':'jack', 'age':22})
    writer.writerow({'id':'1', 'name':'jack', 'age':22})
    writer.writerow({'id':'1', 'name':'jack', 'age':22})
