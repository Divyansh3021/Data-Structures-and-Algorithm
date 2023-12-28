#-----------------Problem: 1626---------------------

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = [[scores[i], ages[i]] for i in range(len(scores))]
        team.sort()
        dp = [team[i][0] for i in range(len(scores))]

        for i in range(len(team)):
            mScore, mAge = team[i]
            for j in range(i):
                score, age = team[j]
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])
        return max(dp)