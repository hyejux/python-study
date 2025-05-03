# 1. 짝수/홀수 판별

var1 = input("1. 아무숫자나 입력 >> ")
if int(var1) % 2 == 0 :
    print("짝수입니다")
else : 
    print("홀수입니다")

# 2. 양수/음수/0 구분
var2 = int(input("2. 아무숫자나 입력 >> "))
if var2 > 0 :
    print("양수입니다")
else :
    if var2 < 0 :
        print("음수입니다")
    else :
        print("0입니다")

# 3. if ~ elif ~ else 사용한 점수 등급 분류

var3 = int(input("3. 당신의 등급을 알려드릴게요! >> "))

if var3 > 100 or var3 > 0:
    print(" 잘못입력하셨습니다")
elif var3 >= 90 :
    print("A 등급")
elif var3 >= 80 :
    print("B 등급")
elif var3 >= 70 :
    print("C 등급")
else :
    print("F 등급")


# 보너스. 삼항연산자로 60점 컷 합격
score = int(input("합격 컷은 60점 입니다 >>"))
result = "합격" if score >= 60 else "불합격"
#[참일 때 값] if [조건] else [거짓일 때 값]
print(result)

# 4. for문으로 1~10 출력

for i in range(1,10) :
    print(i , "반복 도는 중")

for i in range(1,10,2) :
    print(i , "반복 도는 중 --")


# 5. while문으로 1~5 출력
j = 0
while(j < 10) :
    print(j , "번 반복할거야")
    j+=1


# 6. 1~100 중 짝수만 출력

for i in range(1,100) :
    if i % 2 == 0 :
        print(i , "짝수만 출력중")

for i in range(2, 101, 2):  # step 2로 짝수만
    print(i)

print([i for i in range(2, 101, 2)])  # 리스트로 한 줄 출력


# 7. 구구단 2단 출력

for i in range(1,10):
        print(f"{2} x {i} = {2*i}")


# 8. 리스트 요소 하나씩 출력

aa = [1,2,3]

for i in aa:
    print(i)


# 9. break 문 사용해 반복 중단

for i in aa:
    if i == 3:
        break
    print(i , "출력중")

# 10. continue 문 사용해 특정 조건 건너뛰기

for i in range(1,10):
    if(i % 2 == 0):
        continue
    print(i, "아마 홀수만 나올걸 ?")