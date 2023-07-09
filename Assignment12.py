q1>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle_node(head):
    if head is None or head.next is None:
        return None

    slow_ptr = head
    fast_ptr = head
    prev_ptr = None

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    prev_ptr.next = slow_ptr.next
    del slow_ptr

    return head
q2>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_loop(head):
    if head is None or head.next is None:
        return False

    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

q3>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nth_node_from_end(head, n):
    if head is None:
        return None

    first_ptr = head
    second_ptr = head

    # Move first_ptr N nodes ahead
    for _ in range(n):
        if first_ptr is None:
            return None
        first_ptr = first_ptr.next

    # Move both pointers simultaneously
    while first_ptr is not None:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return second_ptr.val

q4>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    stack = []
    current = head

    # Traverse the linked list and store characters in stack
    while current is not None:
        stack.append(current.val)
        current = current.next

    current = head

    # Traverse the linked list again and compare with stack
    while current is not None:
        if current.val != stack.pop():
            return False
        current = current.next

    return True
q5>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_and_remove_loop(head):
    if head is None or head.next is None:
        return

    slow_ptr = head
    fast_ptr = head
    loop_detected = False

    # Detect the loop using Floyd's Cycle Detection Algorithm
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            loop_detected = True
            break

    # If a loop is detected, find the length of the loop
    if loop_detected:
        length = 1
        slow_ptr = slow_ptr.next
        while slow_ptr != fast_ptr:
            length += 1
            slow_ptr = slow_ptr.next

        # Fix the loop by modifying the pointers
        ptr1 = head
        ptr2 = head
        for _ in range(length):
            ptr2 = ptr2.next

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Set the next pointer of the last node of the loop to None
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None


# Create a linked list with a loop: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop back to node 3)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next

# Remove the loop
detect_and_remove_loop(head)

# Check if the loop is removed by printing the linked list
current = head
while current is not None:
    print(current.val, end=" ")
    current = current.next
q6>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def retain_delete(head, M, N):
    if head is None or M <= 0 or N <= 0:
        return head

    current = head
    previous = None

    while current is not None:
        # Retain M nodes
        for _ in range(M):
            if current is None:
                return head
            previous = current
            current = current.next

        # Delete N nodes
        for _ in range(N):
            if current is None:
                break
            current = current.next

        # Adjust pointers to delete N nodes
        previous.next = current

    return head
q7>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_at_alternate_positions(first_head, second_head):
    if first_head is None:
        return second_head

    first_curr = first_head
    second_curr = second_head
    first_next = None

    while first_curr is not None and second_curr is not None:
        first_next = first_curr.next
        first_curr.next = second_curr
        second_curr = second_curr.next
        first_curr.next.next = first_next
        first_curr = first_next

    if second_curr is not None:
        first_curr.next = second_curr

    second_head = None
    return first_head
q8>class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_circular(head):
    if head is None:
        return False

    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False
