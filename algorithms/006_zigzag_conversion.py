from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        x = y = i = 0
        output = defaultdict(str)
        while i < len(s):
            while y<numRows-1 and i<len(s):
                output[y] += s[i]
                y += 1
                i += 1
            while y>0 and i<len(s):
                output[y] += s[i]
                y -= 1
                i += 1
        return ''.join(output.values())

def main():
    test_input = 'PAY'
    numRows = 1
    sol = Solution()
    print sol.convert(test_input, numRows)

if __name__ == "__main__":
    main()
