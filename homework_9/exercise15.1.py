import pandas as pd

df = pd.read_csv('proteomics.summary.tsv', sep='\t')
# print(df)

count_all_sample = (df.min() >= 2)
count_one_sample = (df.max() >= 2)

print("the number of genes with at least two distinct peptides in all samples:", sum(count_all_sample))
print("the number of genes with at least two distinct peptides in at least one sample:", sum(count_one_sample))