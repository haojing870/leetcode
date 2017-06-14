class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        elif len(strs) ==1:
            return strs[0]
        else:
            common = strs[0]
            for i in range(1,len(strs)):
                l = min(len(common),len(strs[i]))
                carry = ''
                j = 0
                while j<l and common[j] == strs[i][j]:
                    carry += common[j]
                    j += 1
                if carry == '':
                    return carry
                else:
                    common = carry
            return common

def main():
    test = [["abc","ab","abdef"],["jane"],["abc","def"]]
    for item in test:
        sol = Solution()
        print sol.longestCommonPrefix(item)


if __name__ == "__main__":
    main()
