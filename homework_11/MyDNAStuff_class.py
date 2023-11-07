class DNASeq:
    def __init__(self, seq="", name=""):
        self.seq = seq
        self.name = name

    def read_seq_from_filename(self, filepath):
        try:
            seq_file = open(filepath)
            dna_seq = ''.join(seq_file.read().split())
            dna_seq = dna_seq.upper()
            self.seq = dna_seq
            self.name = filepath.split()[-1]
        except IndexError:
            print("Error reading file")
            exit(1)

    def is_valid(self):
        valid_nuc = ['A', 'T', 'C', 'G', 'N']
        for nuc in self.seq:
            if nuc not in valid_nuc:
                return False
        return True

    def complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        try:
            return ''.join(complement_dict[base] for base in self.seq)
        except KeyError:
            print("Invalid base")
            exit(1)

    def reversed_complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        return ''.join(complement_dict[base] for base in reversed(self.seq))

    def reverse(self):
        return ''.join(reversed(self.seq))

    def gc_content(self):
        g_count = self.seq.count('G')
        c_count = self.seq.count('C')
        return (g_count + c_count) / len(self.seq) * 100
