
x=int(input())
n=1000-x
coin=[500,100,50,10,5,1]
coin_num=0

for i in range(len(coin)):
    coins=coin[i]

    if n>=coins:
        num=n//coins
        n=n-(num*coins)
        coin_num=coin_num+num


print(coin_num)