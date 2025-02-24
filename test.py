import random

def binSearch(ary,data):
    pos = -1
    start = 0
    end = len(ary)-1
    count = 0
    while start <= end: # start 가 끝보다 커지면 검색실패
        count += 1
        mid = (start+end) // 2
        if data == ary[mid]:
            return (mid,count)
        elif data > ary[mid]:
            start = mid+1
        elif data < ary[mid]:
            end = mid-1
    return (pos,count)

_ary = random.sample([i for i in range(0,100001)],100000)
_data = random.randint(0,100001)
result = binSearch(_ary,_data)
print(f'{_data} (은)는 {result[0]} 위치에 있음')
print(f'## {result[1]}회 검색함')