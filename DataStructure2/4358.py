from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)  # default 값이 0인 딕셔너리
cnt = 0

while True:
    t = input().strip()  # 나무의 이름을 입력받는다.
    # sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아진다.
    # 따라서 .strip()으로 공백을 제거해준다.
    if len(t) == 0:  # 종료조건
        break
    trees[t] += 1  # 나무 종류 +=1
    cnt += 1  # 나무 총 개수 +=1

result = []
# 각 나무의 개수를 전체 나무의 개수로 나눈 후 *100을 하여 백분율을 구한다.
for key, value in trees.items():
    result.append([key, '{:.4f}'.format(value/cnt*100)])
result.sort()  # 정렬
for r in result:
    print(r[0]+" "+str(r[1]))
