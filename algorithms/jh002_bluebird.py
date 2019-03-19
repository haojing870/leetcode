# Others:
# 1) string tokenizer
# 2) rotate array by k
# 3) recommendation system design, key words, Bayesian docuemnt classification



# Given an integer, convert it to binary, reverse each bit,
# convert to decimal then return

def convert_integer(num):
    if num == 0:
        return 1
    elif num < 0:
        sign = -1
        num = -num
    else:
        sign = 1
    digits = []
    while num > 0:
        digits.append(num%2)
        num = num/2
    new_dec = 0
    for i in xrange(len(digits)):
        new_dec += (1-digits[i])*pow(2,i)
    return sign*new_dec

def main():
    test_ints = [0,32,16,24,-32,-23,50]
    for t in test_ints:
        print convert_integer(t)

if __name__ == '__main__':
    main()
