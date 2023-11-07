import sys

from codon_table_class import *
from MyDNAStuff_class import *

seq = DNASeq()
codons = CodonTable()

seq.read_seq_from_filename(sys.argv[1])
codons.read_codons_from_filename(sys.argv[2])

print("name", seq.name, "Sequence:", seq.seq)
print("Reversed sequence:", seq.reverse())
print("Sequence valid status:", seq.is_valid())
print("Complement Sequence:", seq.complement())
print("Reversed complement:", seq.reversed_complement())
print("gc_content:", seq.gc_content())

if codons.startwith(seq.seq):
    print("The sequence is start with start codon")
else:
    print("The sequence is not start with start codon")

for frame in (1, 2, 3):
    print("Frame", frame, "(forward):", codons.translate(seq.seq, frame))
    print("Frame", frame, "(backward):", codons.translate(seq.reversed_complement(), frame))
