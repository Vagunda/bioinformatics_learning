with open("rosalind_gc.txt", "r") as file:

    ID =[]
    GC =[]

    len = 0
    count = 0

    for line in file:
        if line.startswith(">"):
            ID.append(line.replace(">", ""))
            try:
                gc_content = float(count/len*100)
                len = 0
                count = 0
                GC.append(gc_content)
            except:
                continue

        else:
            for base in line:
                if base == "G" or base == "C" or base == "T" or base == "A":
                    len += 1
                    if base == "G" or base == "C":
                        count += 1
                else:
                    continue

    gc_content = float(count/len*100)
    GC.append(gc_content)

    print(ID[GC.index(max(GC))])
    print(GC[GC.index(max(GC))])


file.close()
