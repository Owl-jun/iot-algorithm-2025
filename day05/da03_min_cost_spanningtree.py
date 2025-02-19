# da03_min_cost_spanningtree

# 최소비용 신장트리

from da02_dfs import Graph

class MinCostGraph(Graph):
    def __init__(self, n):
        super().__init__(n)
        self.parent = [i for i in range(n)]  # Union-Find 부모 배열 초기화

    # Union-Find: 부모 찾기
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union-Find: 두 노드 합치기
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a
            return True
        return False

    def makeAry(self):
        # 모든 간선 추출 (중복 제거 위해 i < k 조건 추가)
        ary = [
            [self.graph[i][k], i, k]
            for i in range(self.size)
            for k in range(i + 1, self.size)
            if self.graph[i][k] != 0
        ]

        # 가중치 오름차순 정렬 (최소 신장 트리 목적)
        ary.sort(key=lambda x: x[0])

        mst = []  # 최소 신장 트리 간선 리스트
        total_cost = 0

        # Kruskal 알고리즘 적용
        for weight, start, end in ary:
            if self.union(start, end):  # 사이클 발생 안 하면 MST에 추가
                mst.append([weight, start, end])
                total_cost += weight
                if len(mst) == self.size - 1:  # MST 완성 시 종료
                    break

        print(f"최소 비용: {total_cost}")
        return mst
 

if __name__ == "__main__":
    G2 = MinCostGraph(6)
    # 춘천 서울 속초 대전 광주 부산
    G2.set({0 : [0,10,15,0,0,0]})   # 춘천
    G2.set({1 : [10,0,40,11,50,0]}) # 서울
    G2.set({2 : [15,40,0,12,0,0]})  # 속초
    G2.set({3 : [0,11,12,0,20,30]}) # 대전
    G2.set({4 : [0,50,0,20,0,25]})  # 광주
    G2.set({5 : [0,0,0,30,25,0]})   # 부산


    print(G2)
    print(G2.makeAry())