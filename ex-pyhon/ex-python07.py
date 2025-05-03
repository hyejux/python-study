import os
import csv
# 1. 파일 열고 문자열 쓰기 (`open("a.txt", "w")`)

# var1 = open("test1.txt","r")
var1 = open("test2.txt","w")
var1.write("안녕하세요 test2파일이에요")
var1.close()

# 2. 파일에 여러 줄 쓰기 (`writelines`)

list = ["사과","딸기","멜론"]
with open("test1.txt","w") as var1:
    var1.writelines(list)

# 3. 파일 닫기 (`f.close()`)
# 파일을 다 쓴 후 .close()는 꼭 호출해야 데이터 손실 방지

# 4. `with open()` 구문으로 안전하게 파일 쓰기
# with 구문을 쓰면 자동으로 close() 처리
with open("test2.txt","w") as var2:
    var2.write("자동으로 닫힘")

# 5. 파일 읽기 (`read()`)
with open("test2.txt","r") as var3:
    content = var3.read()
    print(content)

# 6. 줄 단위로 읽기 (`readline()`, `readlines()`)

with open("test1.txt","r") as var4:
    line1 = var4.readline()
    print(line1)

    lines = var4.readlines()
    print(lines)

# 7. 파일 존재 여부 확인 (`os.path.exists`)
if os.path.exists("test1.txt"):
    print("o")
else :
    print("x")


# 8. 파일에 내용 이어쓰기 (`open(..., "a")`)
with open("test1.txt","a") as f:
    f.write("\n abcabc abc")

# 9. 텍스트 파일에서 특정 단어만 출력
with open("test1.txt", "r") as f:
    for line in f:
        if "a" in line:
            print(line.strip())


# 10. CSV 파일 생성 및 읽기 (기초)
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이"])
    writer.writerow(["가나다", "20"])

# CSV 읽기
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)