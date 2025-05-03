from functools import reduce

# 1. 1~10 리스트 만들기 (리스트 내포)

# list = []
# for i in range(1,10):
#     list.append(i)

li = [i for i in range(1,11)]

print(li)

# 2. 제곱 리스트 만들기 (`[x**2 for x in range(10)]`)

# list2 = []
# for i in range(10):
#     list2.append(i**2)

list2 = [i**2 for i in range(10)]
print(list2)

# 3. 짝수만 필터링한 리스트

list3 = [i for i in range(2,11,2)]
list3 = [i for i in range(1,11) if i % 2 == 0]
# for i in range(2,10,2):
#     list3.append(i)

print(list3)

# 4. 2차원 리스트 만들기 (행렬)

list4 = [[i + j*3 for i in range(1,4)] for j in range(3)]
print(list4)

# 5. 문자열 리스트 길이 추출

s1 = ["안녕하세요 파이선이다","zz", "hi"]
print([len(s) for s in s1])

# 6. map()으로 문자열 숫자로 변환


s2 = ["1","2", "3"]
result2 = list(map(int,s2))
print(result2)


# 7. filter()로 5 이상 값 필터링

nums = [1, 3, 5, 7, 9]
result = list(filter(lambda x : x >= 5, nums)) # 	조건에 맞는 값만 걸러냄
print(result)


# 8. reduce()로 누적합 계산
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x+y, nums)   # 전체를 누적 계산해 하나로 줄임
print(total)



# 9. lambda 함수로 정렬 key 설정

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['apple', 'banana', 'cherry']


# 10. 리스트 정렬 (람다로 정렬 기준 변경)

items = [("사과", 3), ("바나나", 1), ("귤", 2)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)  # [('바나나', 1), ('귤', 2), ('사과', 3)]
