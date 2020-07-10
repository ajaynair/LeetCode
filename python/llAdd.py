# Definition for singly-linked list.
import pdb

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getCurrentValFromNode(self, node: ListNode) -> int:
        if node is None:
            return 0

        return node.val

    def addThreeValToNode(self, node: ListNode, val1: int, val2: int, val3: int):
        remainder = 0

        result = val1 + val2 + val3
        if result >= 10:
            remainder = 1
            result = result - 10
        node.val = result

        return remainder

    def createNextNode(self, node: ListNode) -> ListNode:
        if node is None:
            return None

        node.next = ListNode()
        return node.next

    def getNextNode(self, node: ListNode) -> ListNode:
        if node is None:
            return None

        return node.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head: ListNode = ListNode()
        ans = head
        remainder: int = 0
        #pdb.set_trace()
        while True:
            current_val_l1 = self.getCurrentValFromNode(l1)
            current_val_l2 = self.getCurrentValFromNode(l2)
            remainder = self.addThreeValToNode(ans, current_val_l1, current_val_l2, remainder)

            l1 = self.getNextNode(l1)
            l2 = self.getNextNode(l2)
            if l1 is None and l2 is None:
                if remainder == 1:
                    ans = self.createNextNode(ans)
                    self.addThreeValToNode(ans, 0, 0, remainder)
                return head
            ans = self.createNextNode(ans)

s = Solution()

def createListNode(val: []):
    l: ListNode = None

    for v in val:
        l_prev = ListNode(v, l)
        l = l_prev
    return l_prev

def printListNode(head: ListNode):
    node = head
    while node is not None:
        print (node.val)
        node = node.next

h1 = createListNode([2, 4, 3])
h2 = createListNode([7, 0, 8])

printListNode(s.addTwoNumbers(h1, h2))