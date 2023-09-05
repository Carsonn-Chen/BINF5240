sasp = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"
met_codon = "ATG"
#print(sasp)

pos = sasp.find(met_codon)+1

print(pos)

if pos == 1:
    print("The SASP gene start with a Met codon")
else:
    print("The SASP gene dosen't start with a Met codon")

if pos%3 == 1:
    print("The SASP gene have a frame 1 Met codon")
else:
    print("The SASP gene doesn't have a frame 1 Met codon")

sasp_len = len(sasp)
print("There are", sasp_len, "nucleotides in the SASP gene")

count_sasp_acids = sasp_len/3
print("There are", count_sasp_acids, "amino-acids in the SASP protein")

GC_content = (sasp.count('C')+sasp.count('G') / sasp_len)*100
print("the GC content (% G or C nucleotides) of the SASP gene is", GC_content, "%")
