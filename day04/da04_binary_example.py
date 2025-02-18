import os

class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

MEMORY = []
root = None
fnameAry = []

if __name__ == "__main__":
    forderName = 'C:/Program Files/Common Files/'

    """
    dirName = 현재 경로
    subDirList = 하위 디렉토리 목록
    fnames = 파일 목록
    """
    for dirName, subDirList, fnames in os.walk(forderName):
        for fname in fnames :           # 파일 목록에서 파일을 하나씩 꺼낸다.
            fnameAry.append(fname)      # 파일이름 배열에 파일을 넣는다.
    
    node = TreeNode()                   # 노드 생성
    node.data = fnameAry[0]             # 노드 데이터에 첫번째 파일 삽입
    root = node                         # 방금 만든 노드 루트 지정
    MEMORY.append(node)                 # 메모리에 노드 삽입

    dupNameAry = []                     # 중복 파일 배열 생성

    for name in fnameAry[1:]:           # 루트를 제외한 파일들을 name 변수로 꺼낸다.
        node = TreeNode()               # 꺼낸 파일명을 삽입한 노드를 만든다
        node.data = name                # 윗 줄의 연장선

        current = root                  # 현재선택 = 루트
        while True :                    
            if name == current.data:        # 만약 파일명이 선택된 노드의 파일명과 같다면
                dupNameAry.append(name)     # 중복된파일임으로, 중복배열에 삽입
                break                       # 중단
            if name < current.data:         # 만약 파일명이 현재선택된 파일명보다 작다면(오름차순)
                if current.left == None :   # 거기에다가 선택된 노드의 왼쪽 자식이 비엇다?
                    current.left = node     # 너는 이제부터 선택된 노드의 왼쪽 자식이다.
                    MEMORY.append(node)     # 메모리에 넣고 기억하마
                    break                   # 중단 , 다음 파일로
                current = current.left      # 현재선택된 녀석의 왼쪽자식으로 내려간다.
            else:                           # 파일명이 현재선택된 파일명보다 크다면
                if current.right == None :  # 거기에 마침 선택된 노드의 오른쪽 자식이 없다?
                    current.right = node    # 너는 이제부터 선택된 노드의 오른쪽 자식이다.
                    MEMORY.append(node)     # 메모리에 넣고 기억하마
                    break                   # 중단 , 다음 파일로
                current = current.right     # 선택된 노드의 오른쪽으로 내려간다.
    dupDict = {}
    for i in list(dupNameAry):
        if i in dupDict:
            dupDict[i] += 1
        else: dupDict[i] = 1
    dupNameAry = list(set(dupNameAry))      # 중복된 배열을 set함수 (리스트 등의 중복된 요소 제거) 적용 후 리스트로 반환한다.
    print(dupDict)
    print(forderName, '및 그 하위 디렉터리의 중복된 파일 목록 -->')
    print(dupNameAry)
                    
    """
    정리

    MEMORY 배열은 왜 만든거냐, 현재 동작에서 필요없어보인다.

    이 프로그램은 폴더명안의 파일들을 긁어와서, 이진 탐색 트리를 만듦과 동시에 검색을 하고 있다.
    그 후 중복된 값이 나온다면 dupNameAry 리스트에 append하고 마지막에 set으로 중복을 없애고 결과값을 프린트해줍니다.
    """
