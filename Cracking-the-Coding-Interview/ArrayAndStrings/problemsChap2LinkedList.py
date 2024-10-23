# Linked List


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
