import sys
input_manipulation = sys.argv[1]
seq_file = sys.argv[2]
input_seq = ''.join(open(seq_file).read().split())
print("The sequence is", input_seq)

def complement(nuc):
    nucleotides = 'ACTG'
    complements = 'TGAC'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverse(seq):
    newseq = ''
    for i in seq:
        newseq = i + newseq
    return newseq

def reverseComplement(seq):
    seq = seq.upper()
    newseq = ''
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

if input_manipulation.lower() == 'complement':
    new_seq = ''
    for i in input_seq:
        new_seq = new_seq + complement(i)
    print("The complement sequence is", new_seq)

elif input_manipulation.lower() == 'reverse':
    print("the reverse sequence is", reverse(input_seq))

elif input_manipulation.lower() == 'reversecomplement':
    print("The reversecomplement sequence is", reverseComplement(input_seq))
    
