

weights=[1,1,2,3,6,7,30]

num=1

for i in range(len(weights)):
    if num<weights[i]:
        break
    num=num+weights[i]

print(num)