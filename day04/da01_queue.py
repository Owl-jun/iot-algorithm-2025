# da01_queue.py


class my_queue():

    def __init__(self,size):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.front = 0
        self.rear = 0
    
    def __str__(self):
        return f'{self.queue}'

    def enQueue(self,data):
        if self.isFull():
            print('큐가 꽉찼어요')
            return
        self.rear = (self.rear+1) % self.size
        self.queue[self.rear] = data
        print(f'입력된 데이터 : {data} 추가완료 현재 큐 상태 :{self.queue}')

    def deQueue(self):
        if self.isEmpty():
            print('큐가 비었어요')
            return
        self.front = (self.front+1) % self.size
        result = self.queue[self.front]
        self.queue[self.front] = None
        print(f'삭제된 데이터 : {result} 현재 큐 상태 :{self.queue}')
        return result

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if (self.rear+1) % self.size == self.front:
            return True
        return False
    
    def peek(self):
        if self.isEmpty():
            print('큐가 비었습니다')
            return
        return self.queue[self.front+1]
    

queue = my_queue(5)
queue.enQueue('가')
queue.enQueue('나')
queue.enQueue('다')
queue.enQueue('라')
queue.enQueue('마')

queue.deQueue()
queue.enQueue('마')
queue.enQueue('바')
