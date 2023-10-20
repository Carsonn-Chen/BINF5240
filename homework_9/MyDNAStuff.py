def is_start_codon(codon, seq):
    return seq.startswith(codon)

def nuc_compement(nuc):
    nucleotides = 'ACGTacgtNn'
    complements = 'TGCAtgcaNn'
    i = nucleotides.find(nuc)
    if i >= 0:
        return complements[i]
    return nuc
def complement(seq):
    new_seq = ""
    for nuc in seq:
        new_seq += nuc_compement(nuc)


def reversed_complement(seq):
    new_seq = ""
    for nuc in reversed(seq):
        new_seq += nuc_compement(nuc)

