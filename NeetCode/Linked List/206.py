def reversedlinkedlist(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev