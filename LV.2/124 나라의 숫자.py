

# 예제 1

# 클래스는 속성+메소드(움직임이 있는거)

# class UserInfo:
#     #클래스 최초 초기화
#     def __init__(self,name):
#         self.name=name
#     def user_info_p(self):
#         print("Name : ",self.name)
#
# user1=UserInfo("Kim")
# user1.user_info_p()
# user2=UserInfo("Park")
# user2.user_info_p()

# 클래스,인스턴스 차이 중요
# 네임스페이스 : 객체를 인스터스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# self의 이해

# 인스턴스 함수 , 클래스에서 직접 호출.

# 클래스 변수, 인스턴스 변수
# class WareHouse:
#     #클래스 변수
#     stock_num=0
#     def __init__(self,name):
#         self.name=name
#         WareHouse.stock_num+=1
#     def __del__(self):
#         WareHouse.stock_num-=1
#
# user1=WareHouse('kim')
# user2=WareHouse('Park')
# user3=WareHouse('Lee')
#
# print(user1.__dict__)
# print(user2.__dict__)
# print(user3.__dict__)# 클래스 네임스페이스,클래스 변수(공유)
# print(WareHouse.__dict__) #'stock_num': 3,
#
# print(user1.name)
# print(user2.name)
# print(user3.name)
#
# print(user1.stock_num)


# 파이썬 클래스 상세 이해
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성,메소드 사용가능
#
# class Car:
#     """Parent Class"""
#     def __init__(self,tp,color):
#         self.type=tp
#         self.color=color
#
#     def show(self):
#         return 'Car Class "Show Method"'
#
# class BMWCar(Car):
#     """Sub Class"""
#     def __init__(self,car_name,tp,color):
#         super().__init__(tp,color)
#         self.car_name=car_name
#     def show_model(self)->None:
#         return "Your Car Name: %s"%self.car_name
#
#
# class BenzCar(Car):
#     """Sub Class"""
#     def __init__(self, car_name, tp, color):
#         super().__init__(tp, color)
#         self.car_name = car_name
#
#     def show_model(self) -> None:
#         return "Your Car Name: %s" % self.car_name
#
#     def show(self):
#         print(super().show())
#         return "Car Info :%s %s %s"%(self.car_name,self.type,self.color)
#
# # 일반 사용
# model1=BMWCar('520D','sedan','red')
# print(model1.color)#super
# print(model1.type)#super
# print(model1.car_name)#sub
# print(model1.show())#super
# print(model1.show_model())#sub
# print(model1.__dict__)
#
# # Method Overriding
# model2=BenzCar("220D",'SUV','BLACK')
# print(model2.show())
#
# # Parent Method Call
# model3=BenzCar("E-Class","sedan","silver")
# print(model3.show())
#
# # Inheritance Info(상속관계출력)
# print(BMWCar.mro())
# print(BenzCar.mro())

# 다중 상속

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass

print(M.mro())
