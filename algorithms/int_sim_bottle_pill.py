from collections import defaultdict
import random

def sim(n):
    w, h = n, 0
    seq = []
    w_taken = 0
    for i in range(2*n):
        if i==2*n-2:
            return  n - w_taken
        if random.random() <= 1.0*w/(w+h):
            seq.append('w')
            w -= 1
            h += 1
            w_taken += 1
        else:
            seq.append('h')
            h -= 1
            
def main():
    n = 100
    w_left = defaultdict(int)
    for i in range(1000):
        w_left[sim(n)] += 1
    print w_left

if __name__ == '__main__':
    main()
