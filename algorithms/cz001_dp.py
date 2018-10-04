"""
Given a list of positive numbers,
Can only add non-adjacent numbers,
Find the combination with the max sum.

My solution below returns the indices of included ints.
"""

class Solution(object):
    sols = {}
    def maxSum(self, nums):
        i = len(nums)
        
        if i in self.sols.keys():
            return self.sols[i]
        
        if i == 0:
            sol = (0, [])
        elif i == 1:
            sol = (nums[0], [0])
        else:
            minus1_sum, minus1_combo = self.maxSum(nums[:i-1])
            minus2_sum, minus2_combo = self.maxSum(nums[:i-2])
            if minus1_sum >= minus2_sum + nums[i-1]:
                sol = (minus1_sum, minus1_combo)
            else:
                sol = (minus2_sum+nums[i-1], minus2_combo+[i-1])
        self.sols[i] = sol
        return sol

    def maxSumBottomUp(self, nums):
        sols = {}
        for i in range(len(nums)+1):
            if i == 0:
                sols[i] = (0, [])
            elif i == 1:
                sols[i] = (nums[0], [0])
            else:
                mi1_sum, mi1_combo = sols[i-1]
                mi2_sum, mi2_combo = sols[i-2]
                if mi1_sum >= mi2_sum + nums[i-1]:
                    sols[i] = (mi1_sum, mi1_combo)
                else:
                    sols[i] = (mi2_sum+nums[i-1], mi2_combo+[i-1])
        return sols[i]

def main():
    nums = [1,3,2,4,5,1,3]
    t = Solution()
    ans = t.maxSumBottomUp(nums)
    print ans

if __name__ == '__main__':
    main()
