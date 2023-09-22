def isPalindrome(head):
    arr = []

    curr = head

    while curr:
        arr.append(curr.data)
        curr = curr.next
    
    left = 0 
    right = len(arr) - 1

    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
        
    return True
    pass