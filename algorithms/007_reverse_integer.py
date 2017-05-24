class Solution(object):
    def reverse(self, x):
        if x>=0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        flag = 0
        rlist = []
        while x>=10:
            if flag == 0 and num % 10 != 0:
                flag =1
            else:
                rlist.append(x%10)
                x = x / 10
        rlist.append(x)

        reverse = 0
        digits = len(rlist)
        for i in range(digits):
            reverse += rlist[i] * pow(10,digits-i-1)
        return reverse*sign

        """
        :type x: int
        :rtype: int
        """


def main():
    x = 321
    y = Solution()
    print y.reverse(x)

if __name__ == "__main__":
    main()
