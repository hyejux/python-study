class Car():
    """
    Car class
    Author : Lim
    Date : 2025.05.04
    """

    #클래스 변수는 모든 인스턴스가 공유한다
    car_count = 0

    def __init__(self,company,detail):
        self.car_count = 10
        self._company = company
        self._detail = detail
        Car.car_count += 1

    def __str__(self): # 매직메소드 : 편리하게 print 문으로 확인가능, 비공식적, 사용자 레벨 출력
        return 'str : {} - {}'.format(self._company, self._detail)
     
    def __repr__(self): # 객체 표시, 타입 등등 공식적 문자열 표시 , 개발자 레벨 
        return 'repr : {} - {}'.format(self._company, self._detail)
    
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._detail.get('price')))

    def __del__(self):
        Car.car_count -= 1

# self 의미  : 고유값 지시어, 각각 관리 가능
car1 = Car('Ferrari', {'color' : 'white' , 'price' : 400})
car2 = Car('BMW', {'color' : 'black' , 'price' : 200})


# ID 확인
print(id(car1))
print(id(car2))

print(car1._company == car2._company) # F
print(car1 is car2) # F

# dir & __dict__
print(dir(car1)) # 포괄적인 
print(dir(car2))

print()
print()

print(car1.__dict__) # 값을 상세하게 볼 수 있음
print(car2.__dict__)



# 인스턴스 변수 실행
car1.detail_info()
car2.detail_info()
Car.detail_info(car2) # 클래스명으로 접근할때에는 인스턴스(self인자) 넘겨주기

# 비교
print(car1.__class__, car2.__class__) # 클래스 자체 (부모값)
print(id(car1.__class__), id(car2.__class__))


# 클래스 변수 - 언더바를 붙이지 않으면 암묵적인 클래스 변수임을 나타냄 ⭐
print(car1.__dict__) # car_count 는 나오지 않음
print(car2.__dict__)
print(car1.car_count) # 2가 나와야함
print(dir(car1))

# 접근
print(Car.car_count)
print(car1.car_count)

del car2

# 삭제 확인
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 동일한 변수가 있다면 인스턴스 본인 값 출력, 아니면 상위 검색
# 즉 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스변수,부모))