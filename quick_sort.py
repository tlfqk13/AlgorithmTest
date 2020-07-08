import time
import random


def quick_sort_sub(a,start,end):
    if end-start<=0:
        return

    pivot=a[end]#편의상
    i=start

    for j in range(start,end):
        if a[j]<=pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[end]=a[end],a[j]

    quick_sort_sub(a,start,i-1)
    quick_sort_sub(a,i+1,end)


def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1);


def random_number(a):
    n=a
    random_number_list=[]

    while len(random_number_list) !=n:
        a=random.randint(1,n)
        if a not in random_number_list:
            random_number_list.append(a)

    return random_number_list


start=time.time()

d=random_number(10000)
quick_sort(d)
print(d)
print("time : ",time.time()-start);




# start=time.time()
# print("time : ",time.time()-start);