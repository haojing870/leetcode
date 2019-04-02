
def twoSum(nums, target):
    pair_dict = {}
    for i in xrange(len(nums)):
        pair_dict[target-nums[i]] = i
        if pair_dict.get(nums[i]) is not None:
            return [pair_dict[nums[i]],i]

def maxSubarraySum(nums):
    start = 0
    end = len(nums)
    max_sum = sum(nums)
    while end > start:
        if sum(nums[start:end]) > max_sum:
            max_sum = sum(nums[start:end])
        if nums[start] > nums[end-1]:
            end -= 1
        else:
            start += 1
    return max_sum

def longestSubarrayMaxSum(nums):
    start = 0
    end = len(nums)
    max_sum = sum(nums)
    max_len = end - start
    while end > start:
        if sum(nums[start:end]) > max_sum:
            max_sum = sum(nums[start:end])
            max_len = end - start
        if nums[start] > nums[end-1]:
            end -= 1
        else:
            start += 1
    return max_sum, max_len

def reverseInt(integer):
    if integer < 0:
        sign = -1
        integer = -1 * integer
    elif integer == 0:
        return integer
    else:
        sign = 1
    rev = 0
    while integer > 0:
        rev = rev*10 + integer % 10
        integer = integer / 10
    return rev * sign

def comboDif(nums, diff):
    combos = []
    pair_dict = {}
    for i in nums:
        pair_dict[i-diff] = i
        pair_dict[i+diff] = i
        if pair_dict.get(i) is not None:
            combos.append(set([i,pair_dict.get(i)]))
    return combos

def dividerSum(integer):
    dividers = set()
    if integer > 0:
        flag = 1
    if integer < 0:
        flag = -1
        integer = -1 * integer
    i = 1
    while integer/i >= i:
        if integer%i == 0:
            if flag == 1:
                dividers.add(i)
                dividers.add(integer/i)
                dividers.add(-i)
                dividers.add(-integer/i)
            if flag == -1:
                dividers.add(i)
                dividers.add(-integer/i)
                dividers.add(-i)
                dividers.add(integer/i)
        i += 1
    return dividers

# power(9,5)*7, 6 digit number; max pow(9,5)*6
# special cases 1; then min from 10
# Narcissistic number: N-digit non-negative, sum of digit's power N equals itself
def power5SumInt():
    ints = [1]
    for i in xrange(10,pow(9,5)*6):
        add = 0
        tmp = i
        while tmp>0:
            add += pow(tmp%10,5)
            tmp = tmp/10
        if add == i:
            ints.append(i)
    return ints

# Sample till all k elements of a list are NAs
# Return expected sample times
# a sequence of geometric distribution: # of trails needed till one success -> 
import random
import numpy as np
def sampleToNAs(k, R):
    cnts = []
    for i in xrange(R):
        replaced_indices = set()
        cnt = 0
        while len(replaced_indices) < k:
            sampled = random.randint(0,k-1)
            replaced_indices.add(sampled)
            cnt += 1
        cnts.append(cnt)
    return np.mean(cnts)

    random.choice(items)
    random.sample(items,n)

def weightedRandomGenerator(values, weights):
    probs = []
    for i in xrange(len(weights)):
        probs.append(1.0*np.sum(weights[:i+1])/np.sum(weights))
    r = random.uniform(0,1)
    for i in xrange(len(probs)):
        if r <= probs[i]:
            break
    return values[i]

def main():
    print weightedRandomGenerator([3,4,1],[1,1,2])

if __name__ == '__main__':
    main()
