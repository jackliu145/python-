import csv

with open('test.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'jack', '22'])
    writer.writerow(['2', 'jackfdsfd', '26'])
    writer.writerow(['2', 'jackfdsfd', '26'])
    writer.writerow(['2', 'jackfdsfd', '26'])



