# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a new instance of Listnode to save the list to be returned
        list = ListNode()
        temp = list
        
        #Iterate over the linked lists until either of them are null
        while list1!=None and list2!=None:
            if list1.val < list2.val:
                #Set the next value for current node as the current node value of list1
                list.next = list1
                #Set the current node value to the next value in list1
                #The new current node will be the next value of the previous current node
                list1 = list1.next
                #Set the new current node for merged list
                list = list.next
            else:
                list.next = list2
                list2= list2.next
                list = list.next
        
        #The loop will complete once either of the linked lists are over
        #In case that the other linked list has nodes remaining, it can be added to the 
        #next value of current node of merged list since the input lists are already merged
        if list1!=None:
            list.next = list1
        if list2!=None:
            list.next = list2
            
        #Temp contains the empty node that was created at list=ListNode()
        #Temp.next must be returned to return the merged list
        return temp.next