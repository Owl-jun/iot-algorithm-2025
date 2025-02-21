from tkinter import *
def sortQuick(arr,start,end):
    if end <= start :
        return
    
    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high :
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low],arr[high] = arr[high],arr[low]
            low,high = low+1, high-1
    
    mid = low
    sortQuick(arr,start,mid-1)
    sortQuick(arr,mid,end)

def qSort(ary):
    sortQuick(ary,0,len(ary)-1)

date = [18,18,50,22]
qSort(date)

date

window = Tk()
window.title('이미지처리')
window.geometry("600x600")
photo = PhotoImage(file = '.\image\cupdog.png')

photoAry = []
h = photo.height()
w = photo.width()
for i in range(h) :
    for k in range(w) :
        r, g, b = photo.get(i,k)
        value = (r + g + b) // 3
        photoAry.append(value)

dataAry = photoAry[:]
qSort(dataAry)
midValue = dataAry[h*w//2]
print(midValue)
for i in range(len(photoAry)):
    if photoAry[i] <= midValue :
        photoAry[i] = 0
    else :
        photoAry[i] = 255


pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        photo.put(f"#{r:02x}{g:02x}{b:02x}" , (i,k))


paper = Label(window,image=photo)
paper.pack(expand=1, anchor=CENTER)
window.mainloop()