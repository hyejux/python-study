# 1. 두 수 더하는 함수 만들기

def plus(v1,v2):
    result = v1+v2
    return result

hap = plus(1,3)
print(hap)


# 2. 인자 없이 Hello 출력하는 함수

def hello():
    return "Hello"

print(hello())  # Hello



# 3. 기본값 매개변수 사용

def func(v1=0,v2=2):
    return v1+v2

print(func(3))


# 4. 리턴이 없는 함수 (print만 있음)

def hello2():
    print("Hello")

hello2()  # Hello


# 5. 여러 값 리턴 (return a, b)

def re(v1,v2):
    v1 += 2
    v2 += 2
    return v1, v2

print(re(1,2))

# 6. 리스트를 받아 평균 구하는 함수

def avg_score(list):
    return sum(list) / len(list)

print("평균점수" , avg_score([90,90,90,80]))



# 7. 문자열을 받아 거꾸로 출력하는 함수

def ex_list(s1):
    for i in reversed(s1):
        print(i)

def ex_list2(s1):
    print(s1[::-1])

ex_list("안녕하세요")

# 8. 가변 인자 함수 (*args)

def func(*para): #개수 제한 없이 여러 개의 "위치 인자"를 튜플로 받아서 처리리
    result = 0
    for num in para:
        result += num
    return result

print(func(1, 2, 3, 4))  # 10

# 9. 키워드 인자 함수 (**kwargs) 

def func(**kwargs): #이름이 붙은 인자들을 딕셔너리로 받아서 처리
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(name="ka", age=25)
# name = ka
# age = 25


# 10. 재귀함수: 팩토리얼 구현
def factorial(num):
    if (num <= 1):
        return 1
    else :
        return num * factorial(num-1)
    
print(factorial(4))

