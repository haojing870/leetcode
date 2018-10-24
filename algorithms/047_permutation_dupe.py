class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)

        def help(i):
            if i==0:
                return set([()])
            else:
                combo = help(i-1)
                new_combo = set([])
                for c in combo:
                    for k in range(i):
                        new_combo.add(c[:k]+(nums[i-1],)+c[k:])
                return new_combo

        return [list(c) for c in help(l)]

def main():
    test = [[2,3]]
    sol = Solution()
    ans = []
    for t in test:
        ans.append(sol.permuteUnique(t))
    print ans

if __name__ == "__main__":
    main()
