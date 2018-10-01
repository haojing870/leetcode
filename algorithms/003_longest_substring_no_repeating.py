from sets import Set

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        j = l = 0
        S = Set()
        for i in range(len(s)):
            while j<len(s) and s[j] not in S:
                S.add(s[j])
                if j-i+1>l:
                    l = j-i+1
                j += 1
            S.remove(s[i])
        
        return l

def main():
    test_inputs = ['a', ' ', 'abcabcbb', 'bbbbb', 'pwwkew', 'dfoieddfs']
    sol = Solution()
    outputs = []
    for test in test_inputs:
        outputs.append(sol.lengthOfLongestSubstring(test))
    print outputs

if __name__ == "__main__":
    main()

