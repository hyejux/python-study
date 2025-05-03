import math; 
print(math.sqrt(25))                      # 1. 제곱근: 5.

import random; 
(random.randint(1, 10))            # 2. 난수 생성: 1~10 중 랜덤

from datetime import date;
print(date.today())         # 3. 오늘 날짜 출력

import time; 
time.sleep(1); print("1초 후 실행")        # 4. 1초 지연

import sys; 
print(sys.argv)                            # 5. 인자 처리 (명령줄 인자)

# 6. 사용자 정의 모듈 (mymodule.py 내 add 함수 사용) → 
# import mymodule; 
# (mymodule.add(2,3))

import math; 
from math import pi; 
print(pi)            # 7. import vs from-import

import random; 
print(dir(random))                      # 8. dir()로 함수 목록 확인

# import pandas as pd; 
# print(pd.__name__)                # 9. 모듈 별칭 사용
# 10. 문서 검색: https://docs.python.org/3/library/random.html
