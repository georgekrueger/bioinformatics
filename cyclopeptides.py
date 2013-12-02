import sys

weights = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

# p1 is consistent if p2 contains atleast as many of each element as p1
def consistent(p1, p2):
    m1 = {}
    for p in p1:
        if p in m1:
            m1[p] += 1
        else:
            m1[p] = 1

    m2 = {}
    for p in p2:
        if p in m2:
            m2[p] += 1
        else:
            m2[p] = 1

    for p in m1:
        if p not in m2 or m1[p] > m2[p]:
            return False

    return True

def sumArr(arr):
    s = 0
    for a in arr:
        s += int(a)
    return s

seqs = []
def CyclopeptideSequencing(spectrum, pre):
    global seqs
    
    if not consistent(pre, spectrum):
        return

    sum1 = int(spectrum[len(spectrum)-1])
    sum2 = sumArr(pre)
    if sum2 > sum1:
        return
    if sum1 == sum2:
        seqs.append(pre)
        return

    for w in weights:
        CyclopeptideSequencing(spectrum, pre + [str(w)])

f = open('data.txt', 'r')
line = f.readline()
f.close()
spectrum = line.split(' ')
CyclopeptideSequencing(spectrum, [])
output = ""
for seq in seqs:
    output += "-".join(seq) + " "

f = open('out.txt', 'w')
f.write(output)
f.close()


