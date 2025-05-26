def cut(DNA, recog):
    #check that both sequences contain only canonical (‘ACGT’) nucleotides
    nucl=['A','C','G','T'] #canonical (‘ACGT’) nucleotides
    for n in DNA:
        if n not in nucl:
            return ('Error: Invalid nucleotide in DNA sequence')
    for n in recog:
        if n not in nucl:
            return ('Error: Invalid nucleotide in recognition sequence')
    # find the position
    l_recog=len(recog)
    for i in range(0, len(DNA)-l_recog+1):
        win= DNA[i: i+l_recog]
        if win== recog:
            output='DNA sequence position where the restriction enzyme cuts: '+ str(i+1) # the first nucleotide in the DNA sequence is considered to be at position 1, i is from 0, so the position is (i+1)
    return('Not found')


#get input
DNA= 'ATTTCCTGCGTA'
rec= 'ATT'

print(cut(DNA,rec))