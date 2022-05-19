class Node:
    def __init__(self, key=None, index=0):
        self.key = key
        self.index = index
        self.next = self.prev = self


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def insert_after(self, a):
        h = self.head  # 헤드
        p = self.head.prev  # 헤드 이전 노드

        h.prev = a  # 헤드의 이전노드를 a로
        p.next = a  # 헤드이전노드의 다음노드를 a로

        a.prev = p  # a의 이전노드를 p로
        a.next = h  # a의 다음 노드를 헤드로

    def remove(self, x):
        if x == None:  # x를 None으로 만들고
            return
        x.prev.next, x.next.prev = x.next, x.prev  # x다음노드와 x이전노드 이어주기


n = int(input())
balloons = list(map(int, input().split()))
linked = DoublyLinkedList()
for i, balloon in enumerate(balloons, 1):
    linked.insert_after(Node(key=balloon, index=i))  # 양방향 연결리스트에 하나씩 삽입

rm = linked.head.next  # 지울 노드
result = []
while True:
    cnt = rm.key  # 움직일 횟수

    if cnt == None:  # 움직일 횟수가 없다면, 모든 노드가 다 없어진 것이므로 종료
        break
    result.append(rm.index)
    linked.remove(rm)

    if cnt < 0:
        for i in range(abs(cnt)):
            rm = rm.prev
            if rm.index == 0:
                rm = rm.prev
    else:
        for i in range(cnt):
            rm = rm.next
            if rm.index == 0:
                rm = rm.next
print(' '.join(map(str, result)))
