string1 = input("give string:" )
string2 = input("give another string:" )
hamming_distance = 0

for i,j in zip(string1,string2):
    if i == j:
        continue;
    else:
        hamming_distance = hamming_distance + 1

print(hamming_distance)
