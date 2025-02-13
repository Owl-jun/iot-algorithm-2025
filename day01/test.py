myList = [5,4,3,2,1]

def my_selectSort(lst = list):
    
    count = 0
    temp = lst[count]
    while True:
        is_sorted = True
        # 주어진 배열 중에서 최솟값을 찾는다.
        min_index = count
        for i in range(count,len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
                is_sorted = False
        if is_sorted:
            break
        # 그 값을 맨 앞에 위치한 값과 교체한다(패스(pass)).
        lst[count], lst[min_index] = lst[min_index], lst[count]
        # 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.
        # 하나의 원소만 남을 때까지 위의 1~3 과정을 반복한다.
        print(f'{count+1}회차 결과 : {lst}')
        count += 1
        if count == len(lst) - 1:
            break
    return lst

print(my_selectSort(myList))

# result = [1,2,3,4,5]