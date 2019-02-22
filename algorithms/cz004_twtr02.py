# input file: # of flags, dimension MxN
# each row indicates a color, each row has to be the same color,
# adjacent rows no same color
# return if the file has correct flags

class Solution(object):
    def rightFlag(self, M, N, flag):
        rows = flag[1:]
        prior_row_color = -1
        for row in rows:
            row_color = int(row[0])
            if row_color == prior_row_color:
                return False
            for j in range(len(row)):
                if int(row[j]) != row_color:
                    return False
                prior_row_color = row_color
        return True

    def rightFlags(self, flags):
        num_flags = int(flags[0])
        start = 1
        correct_flags = []
        for n in range(num_flags):
            M, N = int(flags[start][0]), int(flags[start][2])
            end = start + N + 1
            correct_flags.append(self.rightFlag(M, N, flags[start:end]))
            start = end
        return correct_flags

def main():
    s = Solution()
    flags = ['3', '3 3', '000', '111', '222',\
             '3 3', '000', '000', '111',\
             '3 3', '000', '111', '002']
    print s.rightFlags(flags)

if __name__ == '__main__':
    main()
