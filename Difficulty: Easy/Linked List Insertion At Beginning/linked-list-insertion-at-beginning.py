#User function Template for python3

class Solution:
    # Function to insert a node at the beginning of the linked list
    def insertAtBegining(self, head, x):
        cur = Node(x)
        
        cur.next = head
            
        return cur


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Read input for each test case
        arr = list(map(int, input().split()))
        x = int(input())  # Value to insert at the beginning

        # Initialize the linked list
        head = Node(arr[0])
        tail = head

        # Create the linked list from the array
        for num in arr[1:]:
            tail.next = Node(num)
            tail = tail.next

        # Create an instance of Solution class
        ob = Solution()

        # Insert node at the beginning and get the updated head
        ans = ob.insertAtBegining(head, x)

        # Print the updated linked list
        printList(ans)

# } Driver Code Ends