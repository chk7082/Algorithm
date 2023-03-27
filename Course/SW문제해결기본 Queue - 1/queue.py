class Queue:
    '''
    class of Queue
    '''
    def __init__(self, size):
        self.size = size
        self.content = [0] * size
        self.front = -1
        self.rear = -1

    def enQueue(self, element):
        self.rear += 1
        self.content[self.rear] = element

    def deQueue(self):
        self.front += 1
        return self.content[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.size - 1

queue = Queue(3)
#print(queue.size, queue.content, queue.front, queue.rear)
#print(queue.isEmpty())

queue.enQueue(1)
queue.enQueue(2)
#print(queue.isFull())
queue.enQueue(3)
#print(queue.size, queue.content, queue.front, queue.rear)
#print(queue.isFull())

print(queue.deQueue())
#print(queue.isEmpty())
print(queue.deQueue())
print(queue.deQueue())