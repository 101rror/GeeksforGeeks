class kQueues:

    def __init__(self, n, k):
        # Initialize your data members
        self.ans = [[] for _ in range(k)]
        self.size = 0
        self.n = n
        

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        self.ans[i].append(x)
        self.size += 1
        

    def dequeue(self, i):
        # Dequeue element from queue number i
        if self.ans[i]:
            self.size -= 1
            return self.ans[i].pop(0)
        else:
            return -1
        

    def isEmpty(self, i):
        # Check if queue i is empty
        if len(self.ans[i]) == 0:
            return True
        return False
        
        
    def isFull(self):
        # Check if array is full
        if self.size == self.n:
            return True
        return False