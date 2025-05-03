# 1. print("Hello, World!") 출력

print("Hello, World!")

# 2. 정수형, 실수형, 문자열 변수 선언하고 출력

var1 = 100
var2 = 100.1
var3 = "100"

print(var1 , var2 , var3)


# 3. input()으로 이름 입력받아 출력
print("이름>>")
var4 = input()
print(var4)


# 4. 두 숫자 더하기: input으로 두 수 받아 더한 결과 출력

print("A>>")
var5 = input()
print("B>>")
var6 = input()

print(int(var5) + int(var6))

# 5. 문자열 연결과 곱셈 ("hi" * 3)

print("hi" * 3)

# 6. type() 함수로 자료형 확인

print(type(var6), type(var1))

# 7. f-string 사용해 출력

print(f"안녕하세요 제 이름은 {var4}")
print(f"아까 연산했던거 {int(var5) + int(var6)}")


# 8. round(), abs(), pow() 사용해 보기

var7 = 1.1345

print("round" , round(var7)) #반올림
print("abs" , abs(var7)) #절댓댓값
print("pow" , pow(var7,3)) #제곱

# 9. 여러 변수 한 줄에 할당 (a, b = 1, 2)

a, b = 1,2
print(a,b)

# 10. 변수 swap: a, b = b, a

var8 = "abc"
var9 = 1234

var8, var9 = var9, var8

# var9 = var8
# var8 = var7

print(var8, var9)