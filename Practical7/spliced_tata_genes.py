import re

splice_site = input("Enter a splice site combination (GTAG, GCAG, or ATAC): ")
if splice_site not in ['GTAG','GCAG','ATAC']:
    print("Not valid splice site.")
    exit()

# Open the input file for reading
input = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
inp = input.read()
input.close()
# open and name the output file
output = open(f"{splice_site}_spliced_genes.fa", "w")

#tata_pattern is TATAWAW (W=A/T)
tata_pattern = re.compile(r'TATA[AT]A[AT]')

# Split gene entries by '>'
GENE_list = re.split(r'^>',inp, flags=re.MULTILINE)
splice = re.compile(splice_site[:2]+ r'.*'+ splice_site[2:])

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

    # Count TATA_box
    total_matches= tata_pattern.findall(sequence)
    count = len(total_matches)
    
    if re.search(splice, sequence) and count>0:
        output.write('>'+ gene_name + ' ' + 'TATA_count:' + str(count) + '\n') 
        output.write(sequence + '\n') 

output.close()