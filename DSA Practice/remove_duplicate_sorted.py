class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate
                current = current.next
        return head

# Helper function to convert list to linked list
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Example usage:
head = array_to_linked_list([1, 1, 2, 3, 3])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print(linked_list_to_array(new_head))  # Output should be [1, 2, 3]
