from tkinter import *
import random

root = Tk()
# 윈도우 창을 다 덮음 -> 그림을 그림
canvas = Canvas(root,width=1000,height=1000,bg='white')
canvas.pack()
# 캔버스 생성 이후

# 1. 기본 원그리기
# cx = 1000//2
# cy = 1000//2
# r = 400
# canvas.create_oval(cx-r,cy-r,cx+r,cx+r,width=2,outline='red')


count = 0
wSize = 1000
radius = 400
colors = ['red','green','blue','black','orange','indigo','violet']

# 2. 프렉탈 원 그리기 재귀함수 선언
def drawCirclue(x,y,r):
    global count
    count += 1
    canvas.create_oval(x-r,y-r,x+r,y+r,width=2,outline=random.choice(colors))

    if r >= 1:  # 아직 매개변수로 받는 반지름이 기본 사이즈보다 크면
        drawCirclue(x-r//2,y,r//2)
        drawCirclue(x+r//2,y,r//2)

drawCirclue(wSize//2,wSize//2,radius)

root.mainloop()