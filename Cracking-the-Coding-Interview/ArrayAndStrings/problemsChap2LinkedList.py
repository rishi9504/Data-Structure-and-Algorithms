# Linked List


# def of linked list for use in functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#  Remove Dups! Write code to remove duplicates from an unsorted linked list.


def removeDups(head):
    seen = set()
    current = head
    while current:
        if current.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.data)
        current = current.next


# How would you solve this problem if a temporary buffer is not allowed?


def removeDupsNoBuffer(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list


def kthToLast(head, k):
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    current = head
    for i in range(count - k - 1):
        current = current.next
    return current


# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access
# to that node.


def deleteMiddle(head):
    """
    This function will delete the middle node from a singly linked list
    :param head: the head of the linked list
    :return: the head of the modified linked list
    """
    # if the list is empty, then there is no middle node to delete
    if head == None:
        return None

    # prev is a pointer that will point to the node right before the middle node
    prev = head
    # set prev's next pointer to point to the head of the list
    prev.next = head

    # slow is a pointer that will move one node at a time
    slow = prev

    # fast is a pointer that will move two nodes at a time
    fast = head

    # while the fast pointer is not None or the fast pointer's next pointer is not None
    while fast != None and fast.next != None:
        # move the slow pointer to the next node
        slow = slow.next
        # move the fast pointer to the node after the next node
        fast = fast.next.next

    # at this point, the slow pointer should be pointing to the node right before the middle node
    # so we can just set the next pointer of the slow pointer to point to the node after the middle node
    slow.next = slow.next.next

    # and we can return the head of the modified linked list
    return prev.next


# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.


def partition(head, x):
    """
    This function will partition a linked list around a value x
    :param head: the head of the linked list
    :param x: the value to partition around
    :return: the head of the modified linked list
    """
    # if the list is empty, then there is nothing to partition
    if head == None:
        return None

    # prev is a pointer that will point to the node right before the partition
    prev = head
    # set prev's next pointer to point to the head of the list
    prev.next = head

    # slow is a pointer that will move one node at a time
    slow = prev

    # fast is a pointer that will move two nodes at a time
    fast = head

    # while the fast pointer is not None or the fast pointer's next pointer is not None
    while fast != None and fast.next != None:
        # move the slow pointer to the next node
        slow = slow.next
        # move the fast pointer to the node after the next node
        fast = fast.next.next

    # at this point, the slow pointer should be pointing to the node right before the partition
    # so we can just set the next pointer of the slow pointer to point to the node after the partition
    slow.next = slow.next.next

    # and we can return the head of the modified linked list
    return prev.next


# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.


def sumLists(head1: ListNode, head2: ListNode):
    """
    This function will add two linked lists together
    :param head1: the head of the first linked list
    :param head2: the head of the second linked list
    :return: the head of the modified linked list
    """
    dummyHead = ListNode(0)
    current = dummyHead
    carry = 0
    while head1 is not None or head2 is not None or carry != 0:
        x = head1.val if head1 is not None else 0
        y = head2.val if head2 is not None else 0
        sum = carry + x + y
        carry = 1 if sum > 9 else 0
        current.next = ListNode(sum % 10)
        current = current.next
        if head1 is not None:
            head1 = head1.next
        if head2 is not None:
            head2 = head2.next
    return dummyHead.next


# Palindrome: Implement a function to check if a linked list is a palindrome.


def isPalindrome(head):
    """
    This function will check if a linked list is a palindrome
    :param head: the head of the linked list
    :return: True if the linked list is a palindrome, False otherwise
    """
    if head is None:
        return True

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare the first and second halves
    left, right = head, prev
    while right:  # Only need to compare until right is exhausted
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


#  Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


def getIntersectionNode(headA, headB):
    """
    This function will find the intersection of two linked lists

    :param headA: the head of the first linked list
    :param headB: the head of the second linked list
    :return: the node that is the intersection of the two linked lists
    """
    # Find the length of the first linked list
    l1, l2 = headA, headB
    # We want to traverse the two linked lists in a loop, until we find the intersection
    while l1 is not l2:
        # If we've reached the end of the first linked list, start traversing the second linked list
        if l1 is None:
            l1 = headB
        # If we've reached the end of the second linked list, start traversing the first linked list
        else:
            l1 = l1.next

        # If we've reached the end of the second linked list, start traversing the first linked list
        if l2 is None:
            l2 = headA
        # If we've reached the end of the first linked list, start traversing the second linked list
        else:
            l2 = l2.next

    # At this point, l1 and l2 should be pointing to the same node, which is the intersection of the two linked lists
    return l1


# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.


def detectLoop(head):
    """
    This function will detect a loop in a linked list
    :param head: the head of the linked list
    :return: the node that is the beginning of the loop
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
