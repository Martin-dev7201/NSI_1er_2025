def adn(L, sequence):
    frequences = {}
    for i in range(len(sequence) - L + 1):
        sous_sequence = sequence[i:i+L]
        if sous_sequence in frequences:
            frequences[sous_sequence] += 1
        else:
            frequences[sous_sequence] = 1
    max_appariations = 0
    meilleur_motif = "" 
    for motif in sorted(frequences.keys()):
        if frequences[motif] > max_appariations:
            max_appariations = frequences[motif]
            meilleur_motif = motif
            
    return meilleur_motif

print(adn(2, 'TCGTACGTAG'))
print(adn(4, 'AATTCGGCCGATCGTCGAATTCGATA'))