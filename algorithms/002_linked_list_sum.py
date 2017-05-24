# Definition of singly-linked list:

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def value_str(self):
        pointer = self
        value_str = ''
        while pointer != None:
            if value_str == '':
                value_str += str(pointer.val)
            else:
                value_str += '->' + str(pointer.val)
            pointer = pointer.next
        return value_str

# learned: python pass by reference
# test case: None+None, None+num, num+Num, 5+5, 243+564

class Solution(object):
    def test(self):
        head = ListNode(1)
        tail = ListNode(2)
        head.next = tail
        tail = head
        head = head.next
        tail.val += 3
        print head.val, tail.val
        head = tail
        tail = tail.next
        tail.val += 3
        print head.val, tail.val

    def addTwoNumbers(self, l1, l2):
        
        head = None
        tail = None
        carry = 0

        while l1 != None or l2 != None or carry != 0:

            addup = ListNode(0)

            if head == None:
                head = addup
            if tail != None:
                tail.next = addup

            if l1 == None and l2 == None:
                addup.val = carry
                return head
            elif l1 == None:
                addup.val = (l2.val + carry) % 10
                carry = (l2.val + carry) / 10
                l2 = l2.next
            elif l2 == None:
                addup.val = (l1.val + carry) % 10
                carry = (l1.val + carry) / 10
                l1 = l1.next
            else:
                addup.val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) / 10
                l1 = l1.next
                l2 = l2.next

            tail = addup

        return head

    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

def main():
    l1 = None
    #l1_2 = ListNode(4)
    #l1_3 = ListNode(3)
    #l1.next = l1_2
    #l1_2.next = l1_3
    #test = l1.value_str()
    #print test

    l2 = ListNode(5)
    #l2_2 = ListNode(6)
    #l2_3 = ListNode(4)
    #l2.next = l2_2
    #l2_2.next = l2_3
    print l2.value_str()

    result = Solution()
    add_sum = result.addTwoNumbers(l1,l2)
    print add_sum.value_str()

if __name__ == "__main__":
    main()
