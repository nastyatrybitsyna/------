class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node_4 = ListNode(-4)

head.next = node2
node2.next = node0
node0.next = node_4
node_4.next = node2  

print(hasCycle(head))  

head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node2.next = head  

print(hasCycle(head))  

head = ListNode(1)
print(hasCycle(head))  
