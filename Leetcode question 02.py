# Leetcode question 2 - Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# for this problem we want to aproch it from a functinal perspective
# take the head of each list and add them. If you have a carry-over bit, carry it.
# Ok that was not functinal but ok!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        if (self.next == None):
            return str(self.val)
        else:
            return str(self.next) + "*" + str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return Solution.addTwoNumbersRec(None, l1, l2)

    def addTwoNumbersRec(self, l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
        if (l1 == None and l2 == None):
            if (carry == 0):
                return None
            else:
                return ListNode(carry)
        elif (l1 == None):
            v = l2.val + carry
            ncarry = v // 10
            v = v % 10
            return ListNode(v, Solution.addTwoNumbersRec(None, None, l2.next, ncarry))
        elif (l2 == None):
            v = l1.val + carry
            ncarry = v // 10
            v = v % 10
            return ListNode(v, Solution.addTwoNumbersRec(None, l1.next, None, ncarry))
        else:
            v = l1.val + l2.val + carry
            ncarry = v // 10
            v = v % 10
            nextNode: ListNode = Solution.addTwoNumbersRec(None, l1.next, l2.next, ncarry)
            return ListNode(v, nextNode)

class Tests:
    @staticmethod
    def Test001():
        assert (Solution.addTwoNumbers(None, None, None) == None)
    
    @staticmethod
    def Test002():
        node = ListNode(7)
        assert (Solution.addTwoNumbers(None, node, None) != None)
        assert (Solution.addTwoNumbers(None, node, None).val == 7)
    
    @staticmethod
    def Test003():
        node = ListNode(6)
        assert (Solution.addTwoNumbers(None, None, node) != None)
        assert (Solution.addTwoNumbers(None, None, node).val == 6)
    
    @staticmethod
    def Test004():
        node1 = ListNode(3)
        node2 = ListNode(2)
        assert (Solution.addTwoNumbers(None, node1, node2) != None)
        assert (Solution.addTwoNumbers(None, node1, node2).val == 5)
    
    @staticmethod
    def Test005():
        node1 = ListNode(5)
        node2 = ListNode(7)
        assert (Solution.addTwoNumbers(None, node1, node2) != None)
        assert (Solution.addTwoNumbers(None, node1, node2).val == 2)
        assert (Solution.addTwoNumbers(None, node1, node2).next != None)
        assert (Solution.addTwoNumbers(None, node1, node2).next.val == 1)
    
    @staticmethod
    def Test006():
        node = ListNode(3, ListNode(7))
        assert (Solution.addTwoNumbers(None, node, None) != None)
        assert (Solution.addTwoNumbers(None, node, None).val == 3)
        assert (Solution.addTwoNumbers(None, node, None).next != None)
        assert (Solution.addTwoNumbers(None, node, None).next.val == 7)
    
    @staticmethod
    def Test007():
        node1 = ListNode(5, ListNode(7))
        node2 = ListNode(5)
        assert (Solution.addTwoNumbers(None, node1, node2) != None)
        assert (Solution.addTwoNumbers(None, node1, node2).val == 0)
        assert (Solution.addTwoNumbers(None, node1, node2).next != None)
        assert (Solution.addTwoNumbers(None, node1, node2).next.val == 8)
    
    @staticmethod
    def Test008():
        # 834 + 83,564 = 84,398
        node1 = ListNode(4, ListNode(3, ListNode(8)))
        node2 = ListNode(4, ListNode(6, ListNode(5, ListNode(3, ListNode(8)))))
        outString = str(Solution.addTwoNumbers(None, node1, node2))
        print(outString)
        assert(outString == "8*4*3*9*8")
    

    @staticmethod
    def Test009():
        # 834 + 83,564 = 84,398
        node1 = ListNode(1)
        node2 = ListNode(9, ListNode(9))
        outString = str(Solution.addTwoNumbers(None, node1, node2))
        print(outString)
        assert(outString == "1*0*0")





Tests.Test001()
Tests.Test002()
Tests.Test003()
Tests.Test004()
Tests.Test005()
Tests.Test006()
Tests.Test007()
Tests.Test008()
Tests.Test009()


# And it works!
# Runtime: 88 ms, faster than 16.85% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.8 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.