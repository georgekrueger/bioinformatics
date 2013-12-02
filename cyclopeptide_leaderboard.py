import sys

masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def mass(pep):
    tot = 0
    for p in pep:
        tot += p
    return tot

def score(pep, spectrum):
    

def LeaderboardCyclopeptideSequencing(spectrum, n):
    leaderboard = [[]]
    leaderPeptide = None

    while len(leaderboard) > 0:
        for pep in leaderboard:
            for mass in masses:
                leaderboard.append(pep + [mass])
        parentMass = spectrum[len(spectrum)-1]
        newLeaderboard = []
        for pep in leaderboard:
            if mass(pep) == parentMass:
                if leaderPeptide is None or score(pep) > score(leaderPeptide):
                    leaderPeptide = pep
                elif mass(pep) > parentMass:
                    continue
                newLeaderboard.append(pep)

        leaderboard = cutLeaderboard(newLeaderboard, spectrum, n)

    print(leaderPeptide)
