class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2listNode(lst):
    head = ListNode(lst.pop(0))

    cur = head
    for el in lst:
        new_node = ListNode(el)
        cur.next = new_node
        cur = new_node

    return head


def printListNode(node):

    out_lst = []
    while node:
        out_lst.append(str(node.val))
        node = node.next
    output_text = " ".join(out_lst)
    print(f"{output_text}")
