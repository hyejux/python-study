# 규모에 따라 , 목적에 따라 클래스기반 / 절차기반을 선택하면 된다
# 객체지향프로그래밍 OOP

# 일반적인 코딩
car_company_1 = 'Ferrari'
car_detail_1 =  [
    {'color' : 'while'},
    {'price' : 400}
]


# 리스트 구조 : 관리하기 불편
car_company_list = ['Ferrari', 'BMW']
car_detail_list = [
       {'color' : 'while' , 'price' : 400},
       {'color' : 'black' , 'price' : 200}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등..

car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : { 'color' : 'while' , 'price' : 400 } },
    {'car_company' : 'BMW', 'car_detail' : {'color' : 'black' , 'price' : 200} }
]

# pop(key)
del car_dicts[1]

print(car_dicts)


# 클래스 구조

class Car():
    def __init__(self,company,detail):
        self._company = company
        self._detail = detail

    def __str__(self): # 매직메소드 : 편리하게 print 문으로 확인가능, 비공식적, 사용자 레벨 출력
        return 'str : {} - {}'.format(self._company, self._detail)
     
    def __repr__(self): # 객체 표시, 타입 등등 공식적 문자열 표시 , 개발자 레벨 
        return 'repr : {} - {}'.format(self._company, self._detail)

car1 = Car('Ferrari', {'color' : 'white' , 'price' : 400})
car2 = Car('BMW', {'color' : 'black' , 'price' : 200})

print(car1) # <__main__.Car object at 0x00000201B59B6900>

print(car1.__dict__)  # 클래스 안 속성 볼 수 있음
print(dir(car1))  # 메타 ?

#리스트 선언

car_list = []

car_list.append(car1)
car_list.append(car2)

print(car_list)


for x in car_list:
    print(repr(x))