import string

# Find all occurrences (overlaps allowed) of a pattern 'pat' in string 's'.
# Allow up to 'd' mismatches
def findPattern(pat, s, d):
    indices = []
    for i in xrange(len(s) - len(pat) + 1):
        mismatches = 0
        for j in xrange(i, i+len(pat)):
            if pat[j-i] != s[j]:
                mismatches += 1
                if mismatches > d:
                    break
        if mismatches <= d:
            indices.append(i)
    return indices

def getAllKmerPermutations(k):
    return getAllKmerPermutationsRec(k, "")
    
def getAllKmerPermutationsRec(k, s):
    if len(s) >= k:
        return [s]
    #print s
    parts = ['A', 'T', 'C', 'G']
    rets = []
    for p in parts:
        s2 = s + p
        rets.extend(getAllKmerPermutationsRec(k, s2))
    return rets

def findFrequentKmerWithMismatch(text, k, d):
    kmers = getAllKmerPermutations(k)
    bests = []
    freq = 0
    for kmer in kmers:
        indices = findPattern(kmer, text, d)
        if len(indices) > freq:
            bests = [kmer]
            freq = len(indices)
        elif len(indices) == freq:
            bests.append(kmer)
    return bests

f = open("stepic_dataset.txt", "r")
line = f.readline().strip().split(' ')
text = line[0]
k = line[1]
d = line[2]
f.close()

print text
print k
print d

perms = getAllKmerPermutations(7)
#print perms
print len(perms)

#kmers = findFrequentKmerWithMismatch(text, k, d)
#print " ".join(kmers)


