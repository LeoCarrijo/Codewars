str = 'GCAT'

def dna_to_rna(dna):
    str = (dna.upper()).replace('T', 'U')
    return str

print(dna_to_rna(str))