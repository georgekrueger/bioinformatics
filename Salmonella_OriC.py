import Skew
import Kmers

if __name__ == "__main__":
    f = open("data\Salmonella_genome.txt", "r")
    #f.readline() # skip first line
    dna = ""
    for line in f:
        dna += line.rstrip()
    f.close()
    print "done reading file"
    
    #winStart = 3818639
    #winEnd = winStart + 500
    #text = dna[winStart:winEnd]
    text = dna
    
    k = 9 # kmer size
    d = 1 # num mismatches
    tree = Kmers.KmerTree(text, k)
    mostFreq = tree.findMostFrequentKmersWithMismatch(d)
    print " ".join(mostFreq)
    