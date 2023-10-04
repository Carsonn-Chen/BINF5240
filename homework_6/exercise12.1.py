import gzip
from Bio import SeqIO


Ref_Seq = {}
total = 0
with gzip.open("human.protein.fasta.gz", "rt") as handle:
    for seq_record in SeqIO.parse(handle, "fasta"):
        for amino_acid in str(seq_record.seq):
            total += 1
            Ref_Seq[amino_acid] = Ref_Seq.get(amino_acid, 0) + 1
for key, value in Ref_Seq.items():
    Ref_Seq[key] = value / total
# print(Ref_Seq)
# print(sum(Ref_Seq.values()))
# print(len(Ref_Seq))

Swiss_Seq = {}
total = 0
with gzip.open("uniprot_sprot_human.xml.gz", "rt") as handle:
    for seq_record in SeqIO.parse(handle, "uniprot-xml"):
        for amino_acid in str(seq_record.seq):
            total += 1
            Swiss_Seq[amino_acid] = Swiss_Seq.get(amino_acid, 0) + 1
for key, value in Swiss_Seq.items():
    Swiss_Seq[key] = value / total
# print(Swiss_Seq)
# print(sum(Swiss_Seq.values()))
# print(len(Swiss_Seq))


Ref_max = max(Ref_Seq.items(), key=lambda x: x[1])
Ref_min = min(Ref_Seq.items(), key=lambda x: x[1])
Swiss_max = max(Swiss_Seq.items(), key=lambda x: x[1])
Swiss_min = min(Swiss_Seq.items(), key=lambda x: x[1])
diff_max = max({x: abs(Ref_Seq.get(x, 0) - Swiss_Seq.get(x, 0)) for x in Ref_Seq.keys()})


print("The most occurs amino acid from Ref_seq is", Ref_max)
print("The least occurs amino acid from Ref_seq is", Ref_min)
print("The most occurs amino acid from Ref_seq is", Swiss_max)
print("The least occurs amino acid from Ref_seq is", Swiss_min)
print("The biggest different amino acid is", diff_max)
