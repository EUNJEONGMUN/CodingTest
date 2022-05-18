n = int(input())
e = list(input())
num = [int(input()) for _ in range(n)]
stack = []


def calculate(a, b, op):  # 계산
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    else:
        return a/b


for i in e:
    if i.isalpha():
        stack.append(num[ord(i)-65])  # 만약에 알파벳이면 append
    else:  # 연산자이면, stack에서 두 개 pop 해서 연산
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, b, i))

print("{:.2f}".format(stack[0]))
