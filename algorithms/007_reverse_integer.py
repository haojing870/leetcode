class Solution(object):
    def reverse(self, x):
        up_bound = pow(2,31) - 1
        low_bound = -pow(2,31)
        
        if x>=0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        flag = 0
        rlist = []
        while x>=10:
            # find the first non-zero digit
            if flag == 0 and x % 10 != 0:
                flag = 1
            rlist.append(x%10)
            x = x / 10
        rlist.append(x)

        reverse = 0
        digits = len(rlist)
        for i in range(digits):
            reverse += rlist[i] * pow(10,digits-i-1)
        reverse = reverse * sign

        if reverse >= low_bound and  reverse <= up_bound:
            return reverse
        else:
            return 0

        """
        :type x: int
        :rtype: int
        """


def main():
    x = -1000000003
    y = Solution()
    print y.reverse(x)

if __name__ == "__main__":
    main()
