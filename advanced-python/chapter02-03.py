class Car():
    """
    Car class
    Author : Lim
    Date : 2025.05.04
    Description: Class, Static, Instance Method
    """

    #클래스 변수는 모든 인스턴스가 공유한다
    price_per_raise = 1.2

    def __init__(self,company,detail):
        # self.car_count = 10
        self._company = company
        self._detail = detail

    def __str__(self): # 매직메소드 : 편리하게 print 문으로 확인가능, 비공식적, 사용자 레벨 출력
        return 'str : {} - {}'.format(self._company, self._detail)
     
    def __repr__(self): # 객체 표시, 타입 등등 공식적 문자열 표시 , 개발자 레벨 
        return 'repr : {} - {}'.format(self._company, self._detail)
    
    # Instance Method
    # self : 객체의 고유한 속석 값을 사용용
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._detail.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._detail.get('price'))
    
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._detail.get('price') * Car.price_per_raise)


    # Class Method : 어노테이션이 붙음, 매개변수는 cls
    @classmethod
    def raise_price(cls, per):
        if per <= 1 :
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increeased.')

    # Static Method : 아무것도 받지 않음 , 유연함 (가끔 쓰는..?)
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not BMW'


# self 의미  : 고유값 지시어, 각각 관리 가능
car1 = Car('Ferrari', {'color' : 'white' , 'price' : 400})
car2 = Car('BMW', {'color' : 'black' , 'price' : 200})


car1.detail_info()
car2.detail_info()

# 가격 정보 (직접 접근)
print(car1._detail.get('price')) # 직접 접근 위험, 캡슐화 , private

# 가격 정보 
print(car1.get_price())

# 가격 인상 (클래스 메소드 미사용) : 좋지 않음음
Car.price_per_raise = 1.4 

# 인상 후 
print(car1.get_price_culc())

# 가격 인상( 클래스 메소드 사용 )
Car.raise_price(1)
print(car1.get_price_culc())

Car.raise_price(1.5)
print(car1.get_price_culc())


# static 메소드 
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

print(Car.is_bmw(car1)) # 이렇게도 가능!
print(Car.is_bmw(car2))