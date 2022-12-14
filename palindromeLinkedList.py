# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        array = []
        while(current != None):
            array.append(current.val)
            current = current.next
        rev = array[::-1]
        for i in range(0, len(array)):
            if array[i] == rev[i]:
                check = True
            else:
                return False        
                break           
        return check  
