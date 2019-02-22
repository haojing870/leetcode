"""
Binary map: get biggest area for connecting 1s.
Input:
    [[0,0,1,1,1,0,0],
     [0,1,1,0,0,1,1],
     [1,1,0,0,1,1,1]]
"""
import Queue

class Solution(object):

    def _search(self, i, j, l, h, binary_map):
        q  = Queue.Queue()
        q.put((i,j))
        binary_map[i][j] = -1
        area = 0
        while not q.empty():
            i,j  = q.get()
            area += 1
            if i-1 >= 0 and binary_map[i-1][j] == 1:
                q.put((i-1,j))
                binary_map[i-1][j] = -1
            if i+1 < h and binary_map[i+1][j] == 1:
                q.put((i+1,j))
                binary_map[i+1][j] = -1
            if j-1 >= 0 and binary_map[i][j-1] == 1:
                q.put((i,j-1))
                binary_map[i][j-1] = -1
            if j+1 < l and binary_map[i][j+1] == 1:
                q.put((i,j+1))
                binary_map[i][j+1] = -1
        return area

    def area(self, binary_map):
        l = len(binary_map[0])
        h = len(binary_map)
        max_area = 0
        for i in range(h):
            for j in range(l):
                if binary_map[i][j] == 1:
                    tmp = self._search(i, j, l, h, binary_map)
                    max_area = tmp if tmp > max_area else max_area
        return max_area

def main():
    binary_map = \
        [[0,0,1,1,1,0,0],\
         [0,1,1,0,0,1,1],\
         [1,1,0,0,1,1,1],\
         [1,1,1,0,1,1,1]]
    t = Solution()
    max_area = t.area(binary_map)
    print max_area

if __name__ == '__main__':
    main()
