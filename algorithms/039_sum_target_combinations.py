class Solution(object):
    def combinationSumBottomUp(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        sol = [[] for _ in range(target+1)]
        sol[0].append([])
        for c in candidates:
            for subtarget in range(len(sol)):
                print c, subtarget, sol
                if sol[subtarget]:
                    if c+subtarget <= target:
                        new_combos = [combo+[c] for combo in sol[subtarget]]
                        sol[subtarget+c].extend(new_combos)
                        print c, subtarget, sol
                    else:
                        break
        return sol[target]

    def combinationSumTopDown(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(left, path, idx):
            print left, path, idx
            if not left:
                res.append(path[:])
            else:
                for i, val in enumerate(candidates[idx:]):
                    if val > left:
                        break
                    dfs(left-val, path+[val], idx+i)
        dfs(target, [], 0)
        return res


def main():
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    combos = sol.combinationSumTopDown(candidates, target)
    print combos

if __name__ == '__main__':
    main()
