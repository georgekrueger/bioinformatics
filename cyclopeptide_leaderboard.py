import sys

masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def mass(pep):
    tot = 0
    for p in pep:
        tot += p
    return tot

def score(pep, spectrum):
    p = sorted(pep)
    s = sorted(spectrum)
    i = 0
    j = 0
    common = 0
    while i < len(p) and j < len(s):
        if p[i] == s[j]:
            common  += 1
            j += 1
            i += 1
        elif p[i] < s[j]:
            i += 1
        elif s[j] < p[i]:
            j += 1
            
    return common
    
#print score([1, 2, 2, 4, 6], [5, 6, 2, 2, 3])
    
# trim leaderboard to the top n peptides based on scoring with spectrum
def trimLeaderboard(leaderboard, spectrum, n):
    scored = []
    for p in leaderboard:
        scored.append((p, score(p[1], spectrum)))
    scored.sort(key=lambda tup: tup[1], reverse=True)
    i = 0
    newLeaderboard = []
    while (i < len(scored) and (i < n or scored[i] == scored[i-1])):
        newLeaderboard.append(scored[i][0])
        i += 1
    return newLeaderboard
    
def leaderboardCyclopeptideSequencing(spectrum, n):
    leaderboard = [[False, []]]
    leaderPeptide = None
    numAddedOnPass = 1
    parentMass = spectrum[len(spectrum)-1]
    print("parentMass: %s" % parentMass)
    passNum = 0
    while len(leaderboard) > 0 and numAddedOnPass > 0:
        numAddedOnPass = 0
        leaderboardLen = len(leaderboard)
        passNum += 1
        print("pass: %s" % passNum)
        for i in range(0, leaderboardLen):
            #print ("leaderboard[i]=%s" % leaderboard[i])
            if leaderboard[i][0] == True:
                # If this item has already been expanded, then don't do it again
                continue
            for m in masses:
                newPep = leaderboard[i][1] + [m]
                if mass(newPep) == parentMass:
                    if leaderPeptide is None or score(newPep, spectrum) > score(leaderPeptide, spectrum):
                        leaderPeptide = newPep
                elif mass(newPep) > parentMass:
                    #print("throw out %s" % mass(newPep))
                    continue
                leaderboard.append([False, newPep])
                #print(leaderboard)
                numAddedOnPass += 1
                # this pep has been expanded
                leaderboard[i][0] = True

        leaderboard = trimLeaderboard(leaderboard, spectrum, n)
        print(len(leaderboard))
        print(numAddedOnPass)

    print("-".join([str(x) for x in leaderPeptide]))
    print("mass of leader: %s" % mass(leaderPeptide))

    
f = open("data.txt")
n = int(f.readline().strip())
spectrum = [ int(x) for x in f.readline().strip().split(" ") ]
print(spectrum)

leaderboardCyclopeptideSequencing(spectrum, n)