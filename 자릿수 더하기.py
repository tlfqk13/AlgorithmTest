
"""
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서
return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
"""
# def solution(n):
#     new = str(n)
#     add = 0
#     for i in range(len(new)):
#         add += int(new[i])
#     return add
#
# n=987
# print(solution(n))


def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

n=118372
print(solution(n))