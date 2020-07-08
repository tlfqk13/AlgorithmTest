import random
import time

def merge_sort(a):
    n=len(a)

    if n<=1:
        return

    mid=n//2
    g1=a[:mid]
    g2=a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1=0
    i2=0
    ia=0

    while i1<len(g1) and i2<len(g2):
        if(g1[i1]<g2[i2]):
            a[ia]=g1[i1]
            i1+=1
            ia+=1

        else:
            a[ia]=g2[i2]
            i2+=1
            ia+=1

    while i1<len(g1):
        a[ia]=g1[i1]
        i1+=1
        ia+=1

    while i2<len(g2):
        a[ia]=g2[i2]
        i2+=1
        ia+=1



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
merge_sort(d)
print(d)

print("time : ",time.time()-start);