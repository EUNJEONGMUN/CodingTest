def len_palindrome(left, right, s):
    length = 0
    while (left >= 0 and right < len(s)):
        if s[left] != s[right]:
            break
        length += 2
        left -= 1
        right += 1
    return length


def solution(s):
    max_length = 1
    for i in range(1, len(s)):
        # i를 기준으로 탐색
        # 팰린드롬의 길이가 홀수라면 -> i번째는 가장 가운데
        # 팰린드롬의 길이라 짝수라면 -> i-1과 i가 가장 가운데
        max_length = max(max_length, len_palindrome(
            i-1, i, s), len_palindrome(i-1, i+1, s)+1)

    return max_length


print(solution("abcdcba"))

print(solution("abacde"))

print(solution("aaa"))
print(solution("abab"))
print(solution("abba"))
print(solution("a"))
