# Give a matrix, 1-bike; 2-scooter; 3-ebike
# Find biggest group

from collections import defaultdict
import Queue as Q

class Solution(object):
    def max_group(self, m):
        l = len(m[0])
        h = len(m)
        q = Q.Queue()
        ms = defaultdict(int)
        for i in range(h):
            for j in range(l):
                v = m[i][j]
                if v != -1:
                    tmp_max = 0
                    q.put((i,j))
                    m[i][j] = -1
                    while not q.empty():
                        i,j = q.get()
                        tmp_max += 1
                        if i-1 >= 0 and m[i-1][j] == v:
                            q.put((i-1,j))
                            m[i][j] = -1
                        if i+1 < h and m[i+1][j] == v:
                            q.put((i+1,j))
                            m[i+1][j] = -1
                        if j-1 >= 0 and m[i][j-1] == v:
                            q.put((i,j-1))
                            m[i][j-1] = -1
                        if j+1 < l and m[i][j+1] == v:
                            q.put((i,j+1))
                            m[i][j+1] = -1
                    if ms[v] < tmp_max:
                        ms[v] = tmp_max
        return ms

def main():
    sol = Solution()
    matrix = [[1,1,1,2,2,3,1],
              [2,2,1,1,3,3,3],
              [1,1,3,3,3,2,1],
              [3,2,1,1,1,1,1]]
    print sol.max_group(matrix)

if __name__ == "__main__":
    main()
