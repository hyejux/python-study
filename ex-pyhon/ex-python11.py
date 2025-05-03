# 1. `class`로 사람(Person) 정의


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



# 2. 생성자(`__init__`)로 name, age 초기화

class Cat:
    def __init__(self):
        self.name = "cat"
        self.age = 1
    
myCat = Cat()

print(myCat.name)
print(myCat.age)


# 3. 메서드 정의 (`self` 사용)

class Dog:
    age = 0
    name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    

myDog = Dog("kevin",10)
print(myDog.getName())



# 4. 객체 생성 및 메서드 호출
print(myDog.name)
print(myDog.age)


# 5. 클래스 변수 vs 인스턴스 변수
class Example:
    class_var = "클래스 변수"  # 모든 인스턴스에 공유됨

    def __init__(self):
        self.instance_var = "인스턴스 변수"  # 각 인스턴스 고유

obj1 = Example()
obj2 = Example()

obj1.instance_var = "바뀐 값"
print(obj2.instance_var)  # 영향 없음

obj1.class_var = "수정된 클래스 변수"
print(obj2.class_var)  # 그대로 (실제로는 새 인스턴스 속성 생긴 것뿐)



# 6. `__str__` 오버라이딩
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # print(person) 시 이 내용 출력됨
        return f"{self.name} ({self.age}살)"

p = Person("kevin", 30)
print(p)  



# 7. 상속 (부모 → 자식 클래스)


class Animal:
    def speak(self):
        return "소리 낸다"

class Dogg(Animal):  # Animal 클래스 상속받음
    def bark(self):
        return "멍멍"

myDogg = Dogg()
print(myDogg.speak())


# 8. 메서드 오버라이딩
class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):  # 부모의 speak()를 덮어씀
        return "야옹"


# 9. 클래스 안에서 리스트로 멤버 관리
class Team:
    def __init__(self):
        self.members = []  # 인스턴스별 멤버 리스트

    def add(self, name):
        self.members.append(name)

    def show(self):
        return ", ".join(self.members)


# 10. `@classmethod`, `@staticmethod` 사용
class Counter:
    count = 0  # 클래스 변수

    @classmethod
    def increment(cls):  # 클래스 자체(cls)에 접근
        cls.count += 1

    @staticmethod
    def hello():  # self, cls 없이 독립적으로 작동
        print("Hello from static method")

Counter.increment()
Counter.increment()
print(Counter.count)
Counter.hello()