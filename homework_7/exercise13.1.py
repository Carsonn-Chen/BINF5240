import pysam

bf = pysam.Samfile('10_Normal_Chr21.bam')

highest_coverage = 0
highest_coverage_locus = None
highest_coverage_counts = None

for pileup in bf.pileup('21'):
    counts = {}
    for pileupread in pileup.pileups:

        if pileupread.indel:
            continue
        if pileupread.is_del:
            continue
        al = pileupread.alignment
        if al.is_unmapped:
            continue
        if al.is_secondary:
            continue
        if int(al.opt('NM')) > 1:
            continue
        if int(al.opt('NH')) > 1:
            continue

        if not pileupread.query_position:
            continue

        readbase = pileupread.alignment.seq[pileupread.query_position]
        if readbase not in counts:
            counts[readbase] = 0
        counts[readbase] += 1

    if len(counts) == 2:
        if sorted(counts.values())[-2] < 10:
            continue
        if pileup.n > highest_coverage:
            highest_coverage = pileup.n
            highest_coverage_locus = pileup.pos
            highest_coverage_counts = counts

if highest_coverage_locus:
    print("Locus:", highest_coverage_locus)
    print("Coverage:", highest_coverage)
    for base, count in highest_coverage_counts.items():
        print("Allele:", base, "Count:", count)
else:
    print("No heterozygous locus found.")
