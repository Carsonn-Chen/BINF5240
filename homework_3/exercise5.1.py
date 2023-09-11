# ctcf ChIP-PCR  primer
ctcf_forward_primer = 'GAGAGGCTGACAGAGAGGAG'
ctcf_reverse_primer = 'CCCATTTCTGCTCCACTTCT'

def complement(nuc):
    nucleotides = 'ACTG'
    complements = 'TGAC'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverseComplement(seq):
    seq = seq.upper()
    newseq = ''
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

print("The reverse complement sequence of ctcf forward primer is", reverseComplement(ctcf_forward_primer))
print("The reverse complement sequence of ctcf reverse primer is", reverseComplement(ctcf_reverse_primer))
