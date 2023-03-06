from math import sqrt
a, b, c = map(float, input().split())


def solution(start, end):
    while start <= end:
        mid = (start+end)/2

        ah = sqrt(a**2-mid**2)
        bh = sqrt(b**2-mid**2)

        value = (ah*bh)/(ah+bh)

        if abs(c-value) < 0.0001:
            return mid
        elif c-value < 0:
            start = mid
        else:
            end = mid


start, end = 0, min(a, b)
print("%0.3f" % solution(start, end))
