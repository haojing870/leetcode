# 1) determine if a string has all unique characters
# what if cannot use additional data structure
# Then the trick is to use array of integers (numpy)

# 2) decide if a string is a permutation of the other
# sorted(str/list/set/dict/tuple, reverse=True/False, key=func)

# 3) replace space to %20 in a string t

# 4) given a string, check if it's a permutation of a palindrome
# from collections import Counter

# 5) 3 edits: replace/remove/insert a character. given 2 strings,
# decide if they're one edit away

# 6) string compression by counts, e.g aabcccccaaa -> a2b1c5a3.
# if compressed is not smaller than orig, return orig

# 7) rotate matrix: given nxn matrix, rotate it in place

# 8) write an algorithm such that if an element in mxn is 0, then
# set its entire row and column to 0

# 9) string rotation: with only 1 call of isSubstring(s1,s2) to 
# check if s1 is a rotation of s2, e.g. watterbottle is a rotation
# of terbottlewat

class Solution(object):
    def unique_char_v1(self, s):
        return len(set(s)) == len(s)

    def check_permutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s1_sort = sorted(s1)
        s2_sort = sorted(s2)
        for i in xrange(len(s1)):
            if s1_sort[i] != s2_sort[i]:
                return False
        return True

    def replace(self, s, orig, new):
        return s.replace(orig, new)

def main():
    sol = Solution()
    test = ['abc','aabbcds','defj']
    for t in test:
        print sol.unique_char_v1(t)
    print sol.check_permutation('abcc', 'ccab')
    print sol.check_permutation('abcd', 'abcc')

if __name__ == '__main__':
    main()
