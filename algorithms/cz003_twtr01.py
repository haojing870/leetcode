# number of times to remove sub from s

class Solution(object):
    def deleteTimes(self, s, sub):
        cnt = 0
        flag = s.find(sub)
        while flag >= 0 and len(s) > 0:
            s = s[:flag] + s[flag+len(sub):]
            cnt += 1
            flag = s.find(sub)
        return cnt

def main():
    s = Solution()
    print s.deleteTimes('abab', 'ab')
    print s.deleteTimes('aaaab','b')
    print s.deleteTimes('abcd','bc')
    print s.deleteTimes('abcd','e')

if __name__ == '__main__':
    main()
