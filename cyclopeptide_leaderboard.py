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
        scored.append((p, score(p, spectrum)))
    scored.sort(key=lambda tup: tup[1], reverse=True)
    i = 0
    newLeaderboard = []
    while (i < len(scored) and (i < n or scored[i] == scored[i-1])):
        newLeaderboard.append(scored[i][1])
        i += 1
        
    return newLeaderboard
    
def leaderboardCyclopeptideSequencing(spectrum, n):
    leaderboard = [[]]
    print(len(leaderboard))
    leaderPeptide = None
    numAddedOnPass = 1
    while len(leaderboard) > 0 and numAddedOnPass > 0:
        print("here")
        numAddedOnPass = 0
        for i in range(0, len(leaderboard)):
            print("!!!")
            for m in masses:
                leaderboard.append(leaderboard[i] + [m])
        print("here2")
        parentMass = spectrum[len(spectrum)-1]
        newLeaderboard = []
        for pep in leaderboard:
            if mass(pep) == parentMass:
                if leaderPeptide is None or score(pep) > score(leaderPeptide):
                    leaderPeptide = pep
                elif mass(pep) > parentMass:
                    continue
                newLeaderboard.append(pep)
                numAddedOnPass += 1
                
        print(numAddedOnPass)

        leaderboard = trimLeaderboard(newLeaderboard, spectrum, n)

    print(leaderPeptide)
    print(leaderboard)

    
f = open("data.txt")
n = int(f.readline().strip())
spectrum = [ int(x) for x in f.readline().strip().split(" ") ]
print(n)
print(spectrum)

leaderboardCyclopeptideSequencing(spectrum, n)