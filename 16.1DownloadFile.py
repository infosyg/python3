import csv
filename = 'd:/learning_python.txt'
with open (filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    