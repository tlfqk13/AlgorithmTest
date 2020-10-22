
# n=626331
# count=0
# arr=[n]
# for i in range(1,9):
# while n>=1:
#     if n%2==0 :
#         n=n/2
#         arr.append(n)
#         print('top',n)
#     if(n==1):
#         n=1
#         break
#     if n%2==1:
#         n=(n*3)+1
#         arr.append(n)
#         print('bot',n)

# def collatz(num):
#     for i in range(500):
#         num=num/2 if num %2 ==0 else num*3+1
#         if num ==1:
#             return i+1
#     return -1

n=18
new=str(n)
sum=0

for i in range(len(new)-1):
    sum=int(new[i])+int(new[i+1])
    if n%sum==0:
        print('true')
    else:
        print('false')

print(sum)

def solution(x):
    answer=True
    new=str(n)
    for i in range(len(new)-1):
        sum=int(new[i])+int(new[i+1])
        if n%sum==0:
            return answer
        else:
            return False