
"""
우리는 A, B, C 3개의 버튼을 적절히 눌러서
그 시간의 합이 정확히 T초가 되도록 해야 한다.
단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다.
이것을 최소버튼 조작이라고 한다.
"""


t=int(input())
btn=[300,60,10]
arr=[]

if t%10==0:
    for i in range(len(btn)):
        btns=btn[i]
        num=t//btns
        t=t-(btns*num)
        arr.append(num)
    print(arr)
else:
    print(-1)
