import sys

n = int(input())
buildings = list(map(int, input().split()))
answer = 0
can_see = [set() for _ in range(n)]


def get_max_high(start, end, position):
    a = (start[1]-end[1])/(start[0]-end[0])
    b = start[1]-(a*start[0])
    hight = a*position+b
    return hight


def can_see_building(start, end):
    for x in range(start[0]+1, end[0]):
        if get_max_high(start, end, x) <= buildings[x]:
            return False
    return True


for i in range(len(buildings)):
    for j in range(i+1, len(buildings)):
        start = (i, buildings[i])
        end = (j, buildings[j])
        if can_see_building(start, end):
            can_see[i].add(j)
            can_see[j].add(i)


max_value = 0
for elem in can_see:
    max_value = max(max_value, len(elem))
print(max_value)
