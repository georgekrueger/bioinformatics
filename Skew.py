
def getSkew(s):
    skew = 0
    skewList = [0]
    for c in s:
        if c == 'C':
            skew -= 1
        if c == 'G':
            skew += 1
        skewList.append(skew)
    return skewList

f = open("data.txt", "r")
s = f.readline()
f.close()
skews = getSkew(s)
#print skews

m = 0
mins = []
i = 0
for sk in skews:
    if sk == m:
        m = sk
        mins.append(i)
    elif sk < m:
        m = sk
        mins = []
        mins.append(i)
    i += 1

print mins
