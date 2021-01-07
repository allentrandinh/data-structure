from heapq import heappush, heappop, heapify


class MinHeap:

    def __init__(self):
        self.heap = []

    #get parent of a node
    def parent(self, i):
        return (i - 1) // 2

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

        # Decrease value of key at index 'i' to new_val

    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])

    def extractMin(self):
        return heappop(self.heap)

        # This functon deletes key at index i. It first reduces

    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

    def display(self):
        print(self.heap)

class MaxHeap(MinHeap):
    #convert all insert key into -key -> minheap turn into maxheap
    #when pop, return the original key

    def insertKey(self, k):
        heappush(self.heap, -k)

    def getMin(self):
        return -self.heap[0]

    def extractMin(self):
        raise RuntimeError("This is a MaxHeap")

    def extractMax(self):
        return -(heappop(self.heap))

    def extractMin(self):
        raise RuntimeError("This is a MaxHeap")

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        return heappop(self.heap)
