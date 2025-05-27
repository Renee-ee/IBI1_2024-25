# INPUT FILES
def read_fasta(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        seq = ''.join([line.strip() for line in lines[1:]])
    return seq
# Read sequences
seq_human = read_fasta('SODM_HUMAN.fasta')
seq_mouse = read_fasta('SODM_MOUSE.fasta')
seq_random = read_fasta('random_sequence.fasta')
# Read BLOSUM62 matrix
blosum62 = {}
with open('BLOSUM62.txt', 'r') as f:
    lines = [line.strip() for line in f if not line.startswith('#')]
    aa = lines[0].split()
    for line in lines[1:]:
        values = line.split()
        row = values[0]
        for i, score in enumerate(values[1:]):
            blosum62[(row, aa[i])] = int(score)


# COMPARE EACH AA
# Calculate alignment score and identity
def align(seq1, seq2):
    score = 0
    identical = 0
    for a, b in zip(seq1, seq2):
        score += blosum62.get((a, b), -4)  # default gap penalty
        if a == b:
            identical += 1
    percent_identity = (identical / len(seq1)) * 100
    return score, percent_identity


# use the function to calculate        
human_mouse = align(seq_human,seq_mouse)
human_random = align (seq_human,seq_random)
mouse_random = align (seq_mouse,seq_random)
# get score and pecentage seperately
human_mouse_score = human_mouse[0]
human_mouse_identical = human_mouse[1]
human_random_score = human_random[0]
human_random_identical = human_random[1]
mouse_random_score = mouse_random[0]
mouse_random_identical = mouse_random[1]

# PRINT OUTPUT
print(f"Human-Mouse: Alignment score={human_mouse_score}, Percentage of identity={human_mouse_identical:.2f}%")
print(f"Human-Random: Alignment score={human_random_score}, Percentage of identity={human_random_identical:.2f}%")
print(f"Mouse-Random: Alignment score={mouse_random_score}, Percentage of identity={mouse_random_identical:.2f}%")