def merge_lists(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.value < head2.value:
        temp = head1
    else:
        temp = head2
    while head1 != None and head2 != None:
        if head1.value < head2.value:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
    if head1 is None:
        temp.next = head2
    else:
        temp.next = head1
    return temp
    pass
