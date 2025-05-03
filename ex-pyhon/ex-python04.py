# 1. 리스트에 숫자 5개 추가하고 출력

a = [1,10,6,4,5]

print(a)

# 2. 리스트에서 최대/최소값 출력

print("최대" , max(a))
print("최소" , min(a))

# 3. 리스트 정렬 (sorted, sort)

a.sort()
print(a)
b = sorted(a)
print(b)

# 4. 튜플 생성하고 요소 출력

c = (1,2,3)

print(c)
print(c[1])

cc = list(c)
cc.append(1234)
c = tuple(cc)

print(c)

# 5. 딕셔너리 생성 후 key로 value 조회

d = {1:"과자", 2:"오이"}
dd = {}

print(d.get(1))
print(dd)

print(d.keys())
print(d.values())
print(d.items())
print(5 in d)
print(d.get(999, "없음"))  # get(key, 기본값)


# 6. 딕셔너리에 새 항목 추가 및 수정

d[3] = "마카롱"
print(d.get(3))

d[3] = "소금"
print(d.get(3))

# 7. 집합(set) 만들고 중복 제거

e = set([1,24,3,24,50])
ee = {1,24,3,24,5}
eee = set()

print(e)
print(ee)
print(list(set([1,2,2,3,3,4])))  # 리스트 중복 제거 후 다시 리스트로



# 8. 두 집합의 교집합, 합집합, 차집합 구하기
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # 교집합: {3}
print(a | b)  # 합집합: {1, 2, 3, 4, 5}
print(a - b)  # 차집합: {1, 2}


# 9. 리스트에 값 삽입, 삭제 (insert, remove)
f = [1,5,6,8,0]
f.insert(2,99)
print(f)

# 10. 리스트 슬라이싱으로 일부만 출력
print(a[1:3])
print(a[:3])
print(a[3:])
print(a[-2:])
print(a[-1])