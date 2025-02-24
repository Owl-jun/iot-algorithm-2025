from operator import itemgetter

books = [['어린왕자','쌩떽쥐베리'],
         ['이방인','까뮈'],
         ['부활','톨스토이'],
         ['신곡','단테'],
         ['돈키호테','세르반테스'],
         ['동물농장','조지오웰'],
         ['데미안','헤르만헤세'],
         ['파우스트','괴테'],['대지','펄벅']]

idx_bookNames = sorted([(book[0],i) for i, book in enumerate(books)],key=itemgetter(0))
idx_writerNames = sorted([(book[1],i) for i, book in enumerate(books)],key=itemgetter(0))

def bookSearch(ary,data):
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start+end)//2
        if data == ary[mid][0]:
            return ary[mid][1]
        elif data > ary[mid][0]:
            start = mid + 1
        else : end = mid - 1
    return pos

getbPos = bookSearch(idx_bookNames,'이방인')
getwPos = bookSearch(idx_writerNames,'까뮈')
print(getbPos)
print(getwPos)