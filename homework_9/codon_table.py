def read_codons_from_filename(filename):
    raw_file = {}
    f = open(filename)
    for i in f:
        tmp = i.split()
        raw_file[tmp[0]] = tmp[2]
    f.close()

    codon_table = {}
    aas_len = len(raw_file['AAs'])
    for i in range(aas_len):
        codon = raw_file['Base1'][i] + raw_file['Base2'][i] + raw_file['Base3'][i]
        codon_table[codon] = {"AAs": raw_file['AAs'][i], "starts": (raw_file['Starts'][i] == 'M')}
    return codon_table


def amino_acid(codon_table, codon):
    return codon_table[codon]['AAs']


def is_init(codon_table, codon):
    return codon_table[codon]['starts']


def get_ambig_aa(codon_table, codon):
    if codon.find('N') != 2:
        return 'X'

    aas = set()
    for n3 in 'ATCG':
        t_codon = codon[:2] + n3
        aas.add(codon_table[t_codon]['AAs'])
    if len(aas) > 1:
        return 'X'
    else:
        return aas.pop()


def translate(codon_table, seq, frame):
    seq += 'N'*(frame-1)
    aa_seq = ""
    for i in range(frame-1, len(seq), 3):
        codon = seq[i:i+3]
        if 'N' in codon:
            aa = get_ambig_aa(codon_table, codon)
        else:
            aa = amino_acid(codon_table, codon)
        aa_seq += aa
    return aa_seq
