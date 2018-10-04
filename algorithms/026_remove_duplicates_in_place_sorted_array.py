class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums

        i = 0
        cnt = 1
        l = len(nums)
        while i+1 < l:
            if nums[i+1] != nums[i]:
                nums[cnt] = nums[i+1]
                cnt += 1
            i += 1
        return nums[:cnt]

def main():
    s = Solution()
    tests = [[2],
             [0,1,1,2,3,3,4,5],
             [1,1,2],
             []]
    output = []
    for t in tests:
        output.append(s.removeDuplicates(t))
    print output

if __name__ == "__main__":
    main()

