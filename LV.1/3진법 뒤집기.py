"""자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를
 return 하도록 solution 함수를 완성해주세요."""


n=45
result=[]

# for i in range(0,4):
#     b = n % 3
#     a = n // 3
#     n=a
#     result.append(b)
# result.reverse()
# d=[]
# for i in range(len(result)):
#     d.append((3**i)*result[i])
#

def solution(n):
    answer=[]
    while True:
        n,rest=divmod(n,3)
        answer.append(rest)
        if n==0:
            break
    return sum([i*3**idx for idx,i in enumerate(reversed(answer))])

print(solution(125))