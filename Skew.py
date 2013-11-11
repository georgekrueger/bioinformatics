
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

def getMinSkews(s):
    skews = getSkew(s)
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
    return mins
    
if __name__ == "__main__":
    f = open("data.txt", "r")
    s = f.readline()
    f.close()
    
