def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #getting the length of LL
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        # print("Length: ",length)

        #getting the target node
        target = length - n + 1
        count = 1
        curr = head

        # print("Target node: ",target)
        prev = None

        while count < target:
            prev = curr
            curr = curr.next
            count += 1

        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        return head