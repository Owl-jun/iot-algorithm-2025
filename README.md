# iot-algorithm-2025
IoT 개발자 자료구조와 알고리즘(코딩테스트) 리포지토리 2025

## 1일차

### 자료구조
- 데이터를 효율적으로 관리하는 방법

#### 자료구조 종류
- 단순 자료구조
    - 정수, 실수, 문자, 문자열
- 선형 자료구조
    - 배열, 리스트, 스택, 큐
- 비선형 자료구조
    - 트리, 그래프
- 파일 자료구조
    - 순차 파일, 색인 파일, 직접 파일

### 알고리즘
- 문제를 해결하는 논리적인 방법, 순서


#### 알고리즘 성능
- **시간복잡도 (빅-오 표기법)** , (빠른 순서로 정렬)
    - $O(1)$ : 데이터 수와 관계없이 항상 일정한 시간 소요
    - $O(log N)$ : 단순 for문인데 전체 중 일부만 처리
    - $O(n)$ : 단순 for문  
    - $O(N\ log N)$ : 2중 for문 인데 내부 for문의 일부만 처리
    - $O(n^2)$ : 2중 for문
    - $O(n^3)$ : 3중 for문
    - $O(2^n)$ : 재귀 호출(팩토리얼, 피보나치) 등

### 리스트 복습
- 1차원, 2차원
    - 리스트 생성, 인덱싱, 슬라이싱, 메서드들 ...
    - 2차원 행, 열 개념, 생성...


## 2일차

- 기초문법
    - 리스트 컴프리핸션 : [노트북](./day02/ds01_list_again.ipynb)

- 자료구조
    - 선형 리스트 : [파이썬](./day02/ds03_linear_list.py)
    - 연결 리스트 : [노트북](./day02/ds04_linked_list.ipynb)