import sys
input_file = sys.argv[1]
f = open(input_file)
seq = f.read().splitlines()
# print(seq)
f.close()

def comp(nuc):
    nucleotides = 'ACGTacgtNn'
    complements = 'TGCAtgcaNn'
    i = nucleotides.find(nuc)
    if i >= 0:
        return complements[i]
    return nuc

def reverse_complement(primer):
    rc = ""
    for n in primer:
        rc = comp(n) + rc
    return rc

result = []
for i in seq:
    tmp = i.split()[0:3]
    # print(repr(tmp))
    tmp[0] = reverse_complement(tmp[0])
    tmp[1] = reverse_complement(tmp[1])
    # print(tmp)
    result.append(' '.join(tmp))

for i in result:
    print(i)
