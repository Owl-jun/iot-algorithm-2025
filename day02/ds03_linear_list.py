# ds03_linear_list.py
# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는게 아님!

# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것!

def add_data(lst,friend):
    lst.append(None)
    lenKatok = len(lst)
    lst[lenKatok-1] = friend

# 중간 데이터 삽입
def insert_data(lst,data,index):
    if index <= len(lst) and index > 0:
        lst.append(None)
        for i in range(len(lst)-1, index, -1):
            lst[i] = lst[i-1]
            lst[i-1] = None

        lst[index] = data

def del_data(lst,index):
    if index > 0 and index < len(lst):
        for i in range(index+1,len(lst)):
            lst[i-1] = lst[i]
            lst[i] = None
        del(lst[len(lst)-1])


# friends = ['다현','쯔위','사나','유리']
# for i in friends:
#     add_data(katok,i)
# print(katok)


# insert_data(katok,'윈터',3)
# print(katok)



# del_data(katok,1)
# print(katok)


sample3 = [[0,20],[1,30],[2,40],[3,50]]
for idx, value in sample3:
    print(f'인덱스{idx} : {value}', end=' ')