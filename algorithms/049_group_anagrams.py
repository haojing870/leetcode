class Solution(object):
    def groupAnagram(self, x):
        if x == 0:
            return True
        elif x<0 or x%10==0:
            return False
        else:
            rev = 0
            num = x
            while num>0:
                rev = rev*10 + num%10
                num = num/10
            return rev == x


def main():
    test = [1221,39400493,0,1,3,4,342,300002,-29384]
    for i in range(len(test)):
        sol = Solution()
        print sol.isPalindrome(test[i])

if __name__ == "__main__":
    main()
