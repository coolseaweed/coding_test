class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_list_node(head):
    val = 0
    cnt = 0
    node = head
    while node:
        print(node.val, cnt)
        val += node.val * 10**cnt
        node = node.next
        cnt += 1

    return val


def add_elements_in_list_node(el_list):
    print(f"el list: {el_list}")
    head = ListNode(el_list.pop(0))

    cur = head
    for el in el_list:
        new_node = ListNode(el)
        cur.next = new_node
        cur = new_node

    return head


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    first = sum_list_node(l1)
    second = sum_list_node(l2)
    total = first + second

    print(f"first: {first} / second: {second} / total: {total}")

    result = []
    for char in str(total):
        result.insert(0, int(char))

    result_list = add_elements_in_list_node(result)
    return result_list


def main():
    # add data
    l1_head = ListNode(2)
    curr_node = l1_head

    new_node = ListNode(4)
    curr_node.next = new_node
    curr_node = new_node

    new_node = ListNode(3)
    curr_node.next = new_node
    curr_node = new_node

    l2_head = ListNode(5)
    curr_node = l2_head

    new_node = ListNode(6)
    curr_node.next = new_node
    curr_node = new_node

    new_node = ListNode(4)
    curr_node.next = new_node
    curr_node = new_node

    result_head = addTwoNumbers(l1_head, l2_head)

    node = result_head
    while node:
        print(node.val)
        node = node.next
    # test_cases = [
    #     ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    #     ([0], [0], [0]),
    #     ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    # ]
    # for test_case in test_cases:
    #     l1, l2, expected = test_case
    #     assert addTwoNumbers(l1, l2) == expected


if __name__ == "__main__":
    main()
