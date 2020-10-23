from collections import deque


bridge_length=2
weight=10
truck_weights=[7,4,5,6]

waiting_truck=[]
ing_bridge=[]
destination=[]

truck_weights=deque(truck_weights)
ing_bridge=deque(ing_bridge)
count=0

# while truck_weights:
#     truck_weights=deque(truck_weights)
#     while truck_weights:
#         tw=truck_weights.popleft()
#         if len(ing_bridge)==0:
#             ing_bridge.append(tw)
#             print('ing', ing_bridge)
#             print('tw',tw)
#         if len(ing_bridge)>=1:
#             if tw+ing_bridge.popleft()<10:
#                 ing_bridge.append(tw)
#                 print('ing1', ing_bridge)
#                 destination.append(tw)
#                 print('dest10',destination)
#             else :
#                 destination.append(tw)
#                 print('dest',destination)


def solution(bride_length,weight,truck_weights):
    answer=0
    bridge=deque([0]*bride_length)
    truck_weights=deque(truck_weights)
    bride_weight=sum(bridge)

    while bridge:
        bride_weight-=bridge[0]
        bridge.popleft()
        answer+=1
        if truck_weights:
            if bride_weight+truck_weights[0]<=weight:
                bride_weight+=truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return answer