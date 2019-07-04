import csv

with open('dict.csv', 'r') as f:
    reader = csv.DictReader(f, lineterminator='\n')
    for row in reader:
        print(dict(row))