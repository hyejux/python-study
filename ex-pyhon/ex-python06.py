# 1. 문자열 길이 출력
str1 = "안녕하세요저는파이썬입니다."
print(len(str1))


# 2. 문자열 인덱싱 (s[0], s[-1])
print(str1[1], str1[2])
print(str1[1] + str1[2])

# 3. 슬라이싱으로 일부 문자열 추출
print(str1[3:4])

# 4. 대소문자 변환 (.upper(), .lower())
str2 = "AbdcADe"

print(str2.upper())
print(str2.lower())

# 5. 공백 제거 (.strip())
str3 = "하 하 호 호 ㅋㅋ . "
print(str3.strip())

# 6. 문자열 나누기 (.split())
str4 = "010-1234-1243"
print(str4.split("-"))


# 7. 문자열 연결 (+ 또는 join)
print(str2+str3)
print("*".join(["010", "1234", "5678"]))  # '010-1234-5678' 리스트나 문자열의 요소들 사이에 삽입


# 8. 특정 단어 포함 여부 ('apple' in s)
print('.' in str3)

# 9. 문자열 바꾸기 (.replace())
print(str4.replace("-","."))

# 10. 문자 개수 세기 (.count())
print(str4.count("-"))
