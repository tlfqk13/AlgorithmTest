
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1

        else:
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1

clothes=[['yellow_hat','headgear'],
         ['blue_sunglasses','eyewear'],
         ['green_turban', 'headgear']]


def solution1(clothes):
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    # ex) output: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    # 위와 같이 딕셔너리가 만들어진다.

    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1

'''각 경우를 다 곱해주면 되는데 
부위별로 있는 옷의 갯수에서 
아무것도 안입는 경우가 있을 수 있으니 +1을 해준다.
 또 모두 안입는 경우는 없다고 했으니 
최종 곱한 값에서 -1을 해준다.
ex) (모자 갯수 + 1) (안경 갯수 + 1) (신발 갯수 + 1) - 1 로 
해주면 되는셈이다.'''

print(solution1(clothes))

