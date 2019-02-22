from collections import defaultdict

class Solution(object):
    def numTreesDP(self,n):
        """
        :type n: int
        :rtype: int
        """
        memo = defaultdict(int)
        def helper(n):
            if n==0:
                memo[0] = 1
                return 1
            if memo[n] > 0:
                return memo[n]
            tmp = 0
            for i in range(1,n+1,1):
                tmp += helper(i-1) * helper(n-i)
            memo[n] = tmp
            return tmp
        return helper(n)

    def numTreesBU(self,n):
        memo = defaultdict(int)
        memo[0] = 1
        for num in range(1,n+1,1):
            tmp = 0
            for i in range(1,num+1,1):
                tmp += memo[i-1] * memo[num-i]
            memo[num] = tmp
        return memo[n]

def main():
    test = [1,2,3,4,5,6,7]
    results = []
    resultsBU = []
    sol = Solution()
    for t in test:
        results.append(sol.numTreesDP(t))
        resultsBU.append(sol.numTreesBU(t))
    print results
    print resultsBU

if __name__ == "__main__":
    main()
