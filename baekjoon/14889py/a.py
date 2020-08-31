n = int(input())
synergies = [list(map(int, input().split())) for _ in range(n)]
people = set([i for i in range(n)])
gap = 40000

def calcDiff(team, enemyTeam):
    global gap
    teamStat = enemyTeamStat = 0
    
    for i in range(n//2):
        for j in range(n//2):
            if i==j: continue
            teamStat += synergies[team[i]][team[j]]
            enemyTeamStat += synergies[enemyTeam[i]][enemyTeam[j]]
    gap = min(gap, abs(teamStat-enemyTeamStat))

def backTracking(team):
    if len(team) >= n/2:
        calcDiff(team, list(people - set(team)))
        return

    for i in range(team[-1]+1, n-n//2+len(team)+1): backTracking(team+[i])

for i in range(n-n//2+2): backTracking([i])
        
print(gap)
