nucl = { "A":"T", "G":"C", "T":"A", "C":"G"}
dna = list(input("give dna string:")[::-1])

for i, j in enumerate(dna):
    dna[i] = nucl[j]

dna = "".join(dna)
print(dna)
