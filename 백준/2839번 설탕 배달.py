

"""
봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지
"""

# inp = int(input())
# Box = 0
# while True:
#     if (inp % 5) == 0:
#         Box = Box + (inp//5)
#         print(Box)
#         break
#     inp = inp-3
#     Box += 1
#     if inp < 0:
#         print("-1")
#         break;

weight=[1,3,5]
t=17
weight_num=0
for i in range(1,len(weight)):
    weights=weight[-i]
    if t>=weights:
        num=t//weights
        t=t-(weights*num)
        weight_num=weight_num+num


print(weight_num)
