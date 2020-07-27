class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Given a linked list defined like this:
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        # I am trying to reverse the entire linked list within O(N) time
        ans = None
        # ans will play a part in the final answer's tail
        while (head != None):
            temp = head.next # temp keeps track of the next item in the linked list
            head.next = ans # grabs the next item in ListNode object and reverses it
            ans = head # changes to next most current location
            head = temp # iterates to the next item in the linked list
        return ans
