class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def addNum(elements):
    head = ListNode(elements[0])
    for el in elements[1:100]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(el)
    return head


def printList(nodeStart):
    ptr = nodeStart
    print('[', end="")
    while ptr:
        print(ptr.val, end=", ")
        ptr = ptr.next
    print(']')


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = None
    temp = None
    c = 0
    while l1 or l2:
        if not l1:
            a = 0
        else:
            a = l1.val
        if not l2:
            b = 0
        else:
            b = l2.val

        n = a+b+c
        c = 1 if n > 9 else 0
        node = ListNode(n % 10)
        if not head:
            head = node
            temp = node
        else:
            head.next = node
            head = node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if c:
        node = ListNode(1)
        head.next = node
    return temp


class Solution:
    pass


obj = Solution()
l1 = addNum([2, 4, 3])
l2 = addNum([5, 6, 4])
printList(addTwoNumbers(l1, l2))