import sys
import csv
import os
import os.path
import math

if len(sys.argv) < 3:
    print("Please enter data file name and gene")
    sys.exit(1)
filename = sys.argv[1]
genename = sys.argv[2]
if not os.path.exists(filename):
    print("Please check filename")
    sys.exit(1)


f = open(filename)
rows = csv.DictReader(f, dialect='excel')
l = {'total': [], '1': [], '2': []}
for i in rows:
    if genename not in i:
        print("Please check gene name")
        sys.exit(1)
    l[i['TUMOUR']].append(float(i[genename]))
    l['total'].append(float(i[genename]))
# print(l)
f.close()

def get_mean_stand(ll):
    mean_value = sum(ll)/ len(ll)
    standard_dev = math.sqrt(sum((x-mean_value)**2 for x in ll) / len(ll))
    return mean_value, standard_dev

print("Total mean and standard_dev:", get_mean_stand(l['total']))
print("mean and standard_dev on Tomour 1:", get_mean_stand(l['1']))
print("mean and standard_dev on Tomour 2:", get_mean_stand(l['2']))