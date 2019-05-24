


def simpCal(input):
    signs = ['+','-','*','/']
    seq_nums = []
    seq_signs = []
    num = ''
    for i in input:
        if i not in signs:
            num += i
        else:
            seq_signs.append(i)
            seq_nums.append(num)
            num = ''
    seq_nums.append(num)
    # process all * & /
    i = 0
    while i < len(seq_signs):
        if seq_signs[i] == '/':
            seq_nums[i] = int(seq_nums[i]) / int(seq_nums[i+1])
            del seq_nums[i+1]
            del seq_signs[i]
        elif seq_signs[i] == '*':
            seq_nums[i] = int(seq_nums[i]) * int(seq_nums[i+1])
            del seq_nums[i+1]
            del seq_signs[i]
        else:
            i += 1
    # process all + & -
    i = 0
    while i < len(seq_signs):
        if seq_signs[i] == '+':
            seq_nums[i] = int(seq_nums[i]) + int(seq_nums[i+1])
            del seq_nums[i+1]
            del seq_signs[i]
        elif seq_signs[i] == '-':
            seq_nums[i] = int(seq_nums[i]) - int(seq_nums[i+1])
            del seq_nums[i+1]
            del seq_signs[i]
        else:
            i += 1

    return seq_nums[0]
    

def main():
    test = '13+2*2*3+1*5-2'
    print simpCal(test)

if __name__ == '__main__':
    main()


