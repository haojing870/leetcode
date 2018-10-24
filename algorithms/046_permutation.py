# Good reference for: recursion vs. DP in 2 formats
# https://blog.csdn.net/u013309870/article/details/75193592

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)

        def help(i):
            if i==0:
                return [[]]
            else:
                combo = help(i-1)
                new_combo = []
                for c in combo:
                    for k in range(i):
                        new_combo.append(c[:k]+[nums[i-1]]+c[k:])
                return new_combo

        return help(l)

def main():
    test = [[], [4], [1,2]]
    sol = Solution()
    ans = []
    for t in test:
        ans.append(sol.permute(t))
    print ans

if __name__ == "__main__":
    main()
