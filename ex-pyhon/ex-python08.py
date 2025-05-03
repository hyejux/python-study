# 1. 0으로 나누기 → try / except ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 2. 문자열 → 숫자 변환 시 에러 처리
try:
    num = int("문자열")
except ValueError:
    print("정수로 변환할 수 없는 문자열입니다.")

# 3. try / except / finally 구조 실습
try:
    print("나누기 시도")
    x = 10 / 2
except ZeroDivisionError:
    print("예외 발생")
finally:
    print("무조건 실행되는 finally 블록")

# 4. else 블록 사용
try:
    num = int("123")
except ValueError:
    print("숫자 변환 실패")
else:
    print(f"변환 성공: {num}")

# 5. 여러 예외 한 번에 처리
try:
    a = int("abc")   # ValueError 발생
    b = 10 / 0       # ZeroDivisionError (실행되지 않음)
except (ValueError, ZeroDivisionError) as e:
    print(f"예외 발생: {e}")

# 6. 사용자 정의 예외 만들기
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# 7. raise 키워드 사용
def check_positive(n):
    if n < 0:
        raise CustomError("음수는 허용되지 않습니다.")
    return n

try:
    check_positive(-5)
except CustomError as e:
    print(f"사용자 정의 예외 발생: {e}")

# 8. 리스트 인덱스 예외 처리
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("리스트 인덱스 범위를 초과했습니다.")

# 9. 파일 열기 실패 처리
try:
    with open("없는파일.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 10. 예외 메시지 출력 (`as e`)
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"예외 메시지: {e}")
