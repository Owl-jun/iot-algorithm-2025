class my_que:
    def __init__(self,size):
        self.start = -1
        self.rear = -1
        self.size = size
        self.que = [None for _ in range(size)]
    
    def __str__(self):
        return f'{self.que}'

    def enQueue(self,data):
        if self.rear < self.size-1:
            self.rear += 1
            self.que[self.rear] = data
           
    def deQueue(self):
        if self.start < self.size-1:
            self.start +=1
            result = self.que[self.start]
            self.que[self.start] = None
        return result
    
    def getStartPosition(self):
        return self.start

    def getRearPosition(self):
        return self.rear
    
    def isEmpty(self):
        if self.start == self.rear : return True
        return False

    def isFull(self):       ## 잘못된 로직
        if self.rear == self.size-1 : return True
        return False
    
    
que = my_que(5)

print(que)
que.enQueue('일놈')
que.enQueue('이놈')
que.enQueue('삼놈')
que.enQueue('사놈')
que.enQueue('오놈')
print(que.isEmpty())
print(que.isFull())
print(que)
ilnom = que.deQueue()
print(que)
que.deQueue()
que.deQueue()
que.deQueue()
que.deQueue()
print(que)
print(que.isEmpty())
print(que.isFull())

