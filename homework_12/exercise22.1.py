from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML

blastp_cline = NcbiblastpCommandline(query="drosoph-ribosome.fasta",
                                     db="yeast-ribosome.fasta",
                                     outfmt=5,
                                     out="blast_results.xml")
stdout, stderr = blastp_cline()

result_handle = open("blast_results.xml")
blast_records = NCBIXML.parse(result_handle)

best_title = ""
best_score = 0
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
                print('****Alignment****')
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('e value:', hsp.expect)
                print(hsp.query[0:75] + '...')
                print(hsp.match[0:75] + '...')
                print(hsp.sbjct[0:75] + '...')

            if hsp.score > best_score:
                best_score = hsp.score
                best_title = alignment.title

result_handle.close()

print("The best reserved:", best_title, best_score)
