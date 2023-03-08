''' Number of possible paths in a m * n matrix where only down and right motion is
is allowed
@mriganka
'''
def  helper(self, m, n, memo):
        c = str(m) + ',' + str(n)
        if c in memo.keys():
            return memo[c]
        if (m == 0) or (n == 0):
            return 0
        if (m == 1) and (n == 1):
            return 1
        memo[c] = self.helper(m, n - 1,memo) + self.helper(m - 1,n,memo)
        return memo[c]
    def numberOfPaths (self, n, m):
        # print(a)
        e = {}
        f = self.helper(m,n,e)
