import re

# Open the input file for reading
input = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
inp = input.read()
input.close()
# Open the output file for writing
output = open("tata_genes.fa", "w")

#tata_pattern is TATAWAW (W=A/T)
tata_pattern = re.compile(r'TATA[AT]A[AT]')

# Split gene entries by '>'
GENE_list = re.split(r'^>',inp, flags=re.MULTILINE)

# Go through each gene entry
for one_gene in GENE_list:
    one_gene = one_gene.strip()
    if one_gene == "":
        continue  # skip empty pieces

    # Extract gene name (before "_mRNA")
    match = re.search(r'^(\S+?)_mRNA', one_gene)
    if match:
        gene_name = match.group(1)
    else:
        gene_name = "Unknown"

    # Extract sequence (thing after the first line)
    lines = one_gene.splitlines()
    sequence = ''.join(lines[1:]) #get sequence lines into one line and skip the first line

    #Search for TATA_box
    if tata_pattern.search(sequence):
        output.write('>'+ gene_name +'\n') # the	header line containing only the gene name
        for i in range(0, len(sequence), 150):
            output.write(sequence[i:i+150] + '\n') # Note that the sequences for each gene run onto several lines.	

output.close()