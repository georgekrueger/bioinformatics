import Skew

if __name__ == "__main__":
    f = open("data\Salmonella_enterica.fasta", "r")
    f.readline() # skip first line
    dna = ""
    for line in f:
        dna += line
    f.close()
    
    skews = Skew.getSkew(dna)
    
    f = open("data\Salmonella_skew.txt", "w")
    i = 0
    for skew in skews:
        if i % 10 == 0:
            s = str(skew)
            f.write(str(i) + " " + s + "\n")
        i += 1
    f.close()
    
    minSkews = Skew.getMinSkews(dna)
    print minSkews
    