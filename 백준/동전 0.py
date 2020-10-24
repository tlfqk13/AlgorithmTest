
"""
첫째 줄에 K원을 만드는데
필요한 동전 개수의 최솟값을 출력한다.
"""
#
# coin=[1,5,10,50,100,500,1000,5000,10000,50000]
# make=4200
# box=0
#
# while True:
#     if make%1000==0:
#         box=box+(make//1000)
#         print(box)
#         break
#     make=make-100
#     box+=1
#     print(make)

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# 최소 동전 개수 구하기
coin_num = 0

for i in range(1, N + 1):
    # 인덱스 끝부터 순회 : 마이너스 인덱스
    coin = coins[-i]

    if K >= coin:
        num = K // coin
        K -= coin * num
        coin_num += num

print(coin_num)