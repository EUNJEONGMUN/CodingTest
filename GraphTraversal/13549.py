from collections import deque

N, K = map(int, input().split())  # N: 언니, K:동생
INF = int(1e9)
second = [INF]*(max(N, K)*2)  # 언니와 동생중 큰 값의 두 배 길이의 second 리스트 생성


def check_range(n):  # 범위 확인
    if n >= 0 and n < (max(N, K)*2):
        return True
    return False


def solution(start, end):
    second[start] = 0
    q = deque()
    if start == end:  # 동생과 언니가 같은 위치에 있다면
        return 0  # 0리턴
    q.append(start)

    while q:  # q가 없을 때 까지
        index = q.popleft()

        move_list = [index*2, index-1, index+1]

        for j in range(3):
            next_node = move_list[j]
            if check_range(next_node):
                if j == 0:  # 만약 순간이동을 한다면 0초 소요
                    if second[next_node] > second[index]:
                        second[next_node] = second[index]
                        q.appendleft(next_node)

                else:  # 만약 +1, -1 이동을 한다면 현재 인덱스의 시간 +1초 소요
                    if second[next_node] > second[index]+1:
                        second[next_node] = second[index]+1
                        q.append(next_node)

    return second[end]


print(solution(N, K))
