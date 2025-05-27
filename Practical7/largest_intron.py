seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

#import necessary library
import re
match = re.search(r'GT.*AG',seq) #search the largest(greedy) sequence start with GT and end with AG

if match:
    matched_seq = match.group() #get that sequence
    max_len = len(matched_seq) # get length of that sequence
    print("the largest length of intron is",max_len)
else: # if haven't found that
    print("No match found.")