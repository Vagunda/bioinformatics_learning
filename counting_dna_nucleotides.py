nucl = dict()
dna_string = input("give dna string:")
for i in dna_string:
    if i not in nucl:
        nucl[i] = 1
    else:
        nucl[i] += 1
print(nucl)
