import sys
from sets import Set

# Returns a dict with all k-mers keyed by string and value
# contains the indices
def findKmers(text, k):
    kmerMap = {}
    for i in xrange(0, len(text)-k):
        subtext = text[i:i+k]
        if subtext in kmerMap:
            kmerMap[subtext].append(i)
        else:
            kmerMap[subtext] = [i]
    return kmerMap

def findKmerClumps(text, k, windowSize, minClumpCount):
    kmerMap = findKmers(text, k)
    foundClumps = []
    for key, indices in kmerMap.iteritems():
        if len(indices) < minClumpCount:
            continue
        # iterate indices
        for i in xrange(len(indices)):
            found = False
            for j in xrange(i+1, len(indices)):
                diff = (indices[j] - indices[i]) + k
                if diff > windowSize:
                    break
                if (j - i) + 1 >= minClumpCount:
                    foundClumps.append(key)
                    found = True
                    break
            if found:
                break
    return foundClumps

k = 9
windowSize = 500
minClumpCount = 3

f = open("data\E-coli.txt", "r")
text = f.readline().strip()
#line = f.readline().strip()
#k = int(line.split()[0])
#windowSize = int(line.split()[1])
#minClumpCount = int(line.split()[2])
f.close()

clumps = findKmerClumps(text, k, windowSize, minClumpCount)
print len(clumps)
#print findKmers(text, k)
            
            
