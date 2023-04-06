# 풀이1 : edges 저장해서 풀기

# from collections import defaultdict

# max_sheep = 0


# def solution(info, edges):
#     trees = defaultdict(list)  # 이진트리 정보 저장
#     visited = [False]*len(info)  # 방문여부
#     for parent, child in edges:
#         trees[parent].append(child)
#     visited[0] = True

#     def dfs(sheep, wolf):
#         global max_sheep

#         if sheep > wolf:
#             max_sheep = max(max_sheep, sheep)
#         else:
#             return
#         for key, values in trees.items():
#             if visited[key]:
#                 for node in trees[key]:
#                     if not visited[node]:
#                         visited[node] = True
#                         if info[node] == 0:
#                             dfs(sheep+1, wolf)
#                         else:
#                             dfs(sheep, wolf+1)
#                         visited[node] = False
#     dfs(1, 0)

#     return max_sheep

# 풀이2 : edges 저장하지 않고 풀기
def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0

        # 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [4, 3], [4, 6],  [6, 5], [
      0, 8], [8, 7], [8, 9], [9, 10], [9, 11]]))
