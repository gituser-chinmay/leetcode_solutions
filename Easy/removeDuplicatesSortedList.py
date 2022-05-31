# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Do operations only if input is not null
        if head is not None:
            #Defining list to perform operations
            temp = head
            
            while temp.next:
                #Since list is sorted, if numbers are repeated they will be next to each other
                if temp.next.val == temp.val:
                    #Re assign the next value to remove duplicate number
                    temp.next = temp.next.next
                else:
                    #Move to next node for comparison
                    temp = temp.next
        return head
