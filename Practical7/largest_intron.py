seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

import re
match = re.search(r'GT.*AG',seq)

if match:
    matched_seq = match.group()
    max_len = len(matched_seq)
    print("the largest length of intron is",max_len)
else:
    print("No match found.")