import time
import random


def bubble_sort(a):
    n=len(a)

    for j in range(0,n-1):
         for i in range(0,n-j-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]

def random_number(a):
    n=a
    random_number_list=[]

    while len(random_number_list) !=n:
        a=random.randint(1,n)
        if a not in random_number_list:
            random_number_list.append(a)

    return random_number_list


start=time.time()

d=[6,8,3,9,10]
bubble_sort(d)
print(d)
print("time : ",time.time()-start);




# start=time.time()
# print("time : ",time.time()-start);