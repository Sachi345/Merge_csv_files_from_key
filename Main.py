import csv
import itertools

with open('output.txt') as file1:
    next(file1)
    rows = (line.strip().split('\t') for line in file1)
    new_file_1 = {row[0]: row[0:] for row in rows}

    # print(new_file_1)

with open('output_file_2.txt') as file2:
    next(file2)
    rows = (line.strip().split('\t') for line in file2)
    new_file_2 = {row[0]: row[1:] for row in rows}

    # print(new_file_2)


def merge(d1, d2):
    d3 = {}

    for k in sorted(d1):
        d3[k] = d1[k], d2[k]
    return d3


d3 = merge(new_file_1, new_file_2)
value = d3.values()
print(value)


header = ['cus_no', 'fname', 'sname', 'age', 'counrty']
with open('merged.txt', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(header)
    writer.writerows(list(itertools.chain(*t)) for t in value)









