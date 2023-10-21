from MyDNAStuff import *
from codon_table import *
import sys

if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

table = read_codons_from_filename(sys.argv[1])
seq = read_seq_from_filename(sys.argv[2])

print("Sequence:", seq)
print("Sequence valid status:", is_valid(seq))
print("Complement Sequence:", complement(seq))
print("Reversed complement:", reversed_complement(seq))
print("gc_content:", gc_content(seq))

if is_init(table, seq[:3]):
    print("Initial codon is a translation start codon.")

for frame in (1, 2, 3):
    print("Frame", frame, "(forward):", translate(table, seq, frame))