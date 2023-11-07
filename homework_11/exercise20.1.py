from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez


def search_human_brca2_refseq():
    Entrez.email = "xl726@georgetown.edu"

    query = "Homo sapiens[Organism] AND BRCA2[Gene Name] AND REFSEQ"
    handle = Entrez.esearch(db="protein", term=query)
    record = Entrez.read(handle)
    handle.close()

    return record["IdList"]


def fetch_protein_sequences(id_list):
    handle = Entrez.efetch(db="protein", id=id_list, rettype="fasta")
    fasta_records = handle.read()
    handle.close()
    return fasta_records


brca2_ids = search_human_brca2_refseq()
print(brca2_ids)
brca2_fasta = fetch_protein_sequences(brca2_ids)

save_file = open("brca2_sequences.fasta", "w")
save_file.write(brca2_fasta)
save_file.close()
