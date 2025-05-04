# 매직 메소드 (스페셜 메소드)
# 파이썬 핵심
# 1 시퀀스 Sequence
# 2 반복 Iterator
# 3 함수 Functions
# 4 클래스 Class

# 클래스 안에 정의할 수 있는 특정한(Built-in) 메소드
# low 레벨에서의 클래스들을 사용해서 좀 더 깊게 개발 가능
# __@@__ 로 되어있는 클래스


# 기본형
print(int(10))
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))

n = 10
print(type(n))

print(n+100)

# 내부적으로 어떤게 호출되었을까? 
print(n.__add__(100)) #내부적으로 해당 함수가 호출되는 것
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1

# 매직메소드를 통해 객체 별 로직도 쉽게 구현가능

class Fruit:
    def __init__(self, name, price):
            self._name = name
            self._price = price
    
    def __str__(self):
          return 'Fruit Class Info : {}, {}'.format(self._name, self._price)

    def __add__(self, x):
          print('called >> __add__')
          return (self._price + x._price) * 0.8
    
    def __sub__(self, x):
          print('called >> __sub__')
          return (self._price - x._price)
    
    def __le__(self,x):
          print('called >> __sub__')
          if self._price <= x._price:
                return True
          else :
                return False
          
    def __ge__(self,x):
          print('called >> __ge__')
          if self._price >= x._price:
                return True
          else :
                return False      
          

# 인스턴스 생성
s1 = Fruit('Orange', 4000)
s2 = Fruit('Banana', 3000)

print(s1 + s2)

# 일반적인 계산
print(s1._price + s2._price)


# 매직메소드
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)

