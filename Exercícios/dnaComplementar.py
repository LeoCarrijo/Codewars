def DnaComplementar(dna):
    dnaComp = ''
    for letra in dna:
        if letra == 'T':
            dnaComp += 'A'
        elif letra == 'A':
            dnaComp += 'T'
        elif letra == 'C':
            dnaComp += 'G'
        elif letra == 'G':
            dnaComp += 'C'
    print(dna)
    return dnaComp
    
print(DnaComplementar('TAAGC'))