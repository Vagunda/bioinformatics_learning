dna = input("give dna string:" )
substring = input("give substring:" )
locations = []

for i,j in enumerate(dna):
    if substring == dna[i:(i + len(substring))]:
        locations.append(i+1)
    else:
        continue

print(*locations)
