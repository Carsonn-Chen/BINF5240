class CodonTable:
    def __init__(self, codon_table = {}):
        self.codon_table = codon_table

    def read_codons_from_filename(self, filename):
        raw_file = {}
        with open(filename) as f:
            for line in f:
                tmp = line.split()
                try:
                    raw_file[tmp[0]] = tmp[2]
                except IndexError:
                    print("Invalid format codon table file")
                    exit(1)

        codon_table = {}
        aas_len = len(raw_file['AAs'])
        for i in range(aas_len):
            codon = raw_file['Base1'][i] + raw_file['Base2'][i] + raw_file['Base3'][i]
            codon_table[codon] = {"AAs": raw_file['AAs'][i], "starts": (raw_file['Starts'][i] == 'M')}
        self.codon_table = codon_table

    def amino_acid(self, codon):
        try:
            return self.codon_table[codon]['AAs']
        except KeyError:
            print("Unknown codon", codon)
            exit(1)

    def is_init(self, codon):
        return self.codon_table[codon]['starts']

    def get_ambig_aa(self, codon):
        if codon.find('N') != 2:
            return 'X'

        aas = set()
        for n3 in 'ATCG':
            t_codon = codon[:2] + n3
            aas.add(self.codon_table[t_codon]['AAs'])
        if len(aas) > 1:
            return 'X'
        else:
            return aas.pop()

    def translate(self, seq, frame):
        seq += 'N' * (frame - 1)
        aa_seq = ""
        for i in range(frame - 1, len(seq), 3):
            codon = seq[i:i + 3]
            if 'N' in codon:
                aa = self.get_ambig_aa(codon)
            else:
                aa = self.amino_acid(codon)
            aa_seq += aa
        return aa_seq

    def startwith(self, seq):
        return self.is_init(seq[0:3])
