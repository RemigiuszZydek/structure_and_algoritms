class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_listnode(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    def to_list(head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst