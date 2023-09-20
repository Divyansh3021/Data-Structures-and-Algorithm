def hasCycle(self, head: Optional[ListNode]) -> bool:
        i, j = head, head

        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                print("i: ",i.val," j: ",j.val)
                return True
        
        else:
            return False