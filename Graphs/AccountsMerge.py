#-----------Problem: 721-----------

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self,n1, n2):
        par1, par2 = self.find(n1), self.find(n2)
        if par1 == par2:
            return False
        
        if self.rank[par1] >= self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
                
        emailGroup = defaultdict(list)
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res