
class my_queue:
    def __init__(self,size):
        self.start = 0
        self.rear = 0
        self.size = size
        self.queue = [None for _ in range(size)]
    
    def __str__(self):
        return f'{self.queue}'

    def enQueue(self,data):
        if self.isFull():
            return
        self.rear = (self.rear+1) % self.size
        self.queue[self.rear] = data
           
    def deQueue(self):
        if self.isEmpty():
            return
        self.start = (self.start+1) % self.size
        result = self.queue[self.start]
        self.queue[self.start] = None
        return result
    
    def getStartPosition(self):
        return self.start

    def getRearPosition(self):
        return self.rear
    
    def isEmpty(self):
        if self.start == self.rear : return True
        return False

    def isFull(self):       
        if (self.rear+1) % self.size == self.start:
            return True
        return False
            
    def peek(self):
        if self.isEmpty():
            print('큐가 비었습니다')
            return
        return self.queue[self.start+1]
    

que = my_queue(5)

print(que)
que.enQueue('일놈')
que.enQueue('이놈')
que.enQueue('삼놈')
que.enQueue('사놈')
que.enQueue('오놈')
print(que.peek())
print(que.isEmpty())
print(que.isFull())
print(que)
ilnom = que.deQueue()
print(que)
que.deQueue()
que.deQueue()
que.enQueue('별놈')
print(que)
print(que.isEmpty())
que.deQueue()
que.deQueue()
print(que.isFull())
print(que)

