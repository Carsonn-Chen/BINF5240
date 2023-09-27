import sys
import csv
import os
import os.path
import math

if len(sys.argv) < 3:
    print("Please input datafile name and gene")
    sys.exit(1)

filename = sys.argv[1]
genename = sys.argv[2]

if not os.path.exists(filename):
    print("Please check filename")

f = open(filename)
rows = csv.DictReader(f, dialect='excel')
l = []
for i in rows:
    l.append(float(i.get(genename, -520)))
# print(l)

mean_value = sum(l)/ len(l)
standard_dev = math.sqrt( sum((x-mean_value)**2 for x in l) / len(l))

print("The mean value is", mean_value)
print("The standard deviation is", standard_dev)
