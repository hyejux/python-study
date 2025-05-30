# 객체 -> 파이썬의 데이터를 추상화 (모델링링)
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0 , 5.0)
pt2 = (2.5 , 1.5)


from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)


# named tuple 튜플인데 딕셔너리 성질을 가짐

from collections import namedtuple


# 네임드 튜플 선언

Point = namedtuple('Point', 'x y') #띄어쓰기로 구분
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)


# print(pt3[0])
# print(pt3.x)
# print(pt4)

l_leng1 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) 
print(l_leng1)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  #Default = False 중복키, 예약어라도 자동으로 다른변수로 선언돼서 생성됨됨

# 출력
print(Point4)

# Dict to Unpacking
temp_dict = {'x':75 , 'y':55} 



#객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20,40)
p3 = Point3(45, y=20)
p4 = Point4(10,20,30,40)
p5 = Point3(**temp_dict) # 언팩킹

print()

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


# 사용
print(p1[0] + p2[1])
print(p1.x + p2.x) 


#Unpacking
x, y = p3

print(x,y)

#네임드 튜플 메소드

temp = [52,38]

#_make() 새로운 객체 생성
p4 = Point1._make(temp)

print(p4)

#_fields 필드 네임 확인
print(p1._fields, p2._fields)

#_asdict() : OrderedDict 반환 - 정렬상태의 딕셔너리를 반환해줌
print(p1._asdict())


# 실 사용 실습
# 반 20명, 4개의 반 

Classes = namedtuple('Classes', ['rank','number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)


# List Comprehension
students = [Classes(rank,number) for rank in ranks for number in numbers]

print(len(students))
print(students)


# 추천 (가독성)
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                  for number in [str(n)
                        for n in range(1,21)]]


# 출력

for s in students2:
    print(s)