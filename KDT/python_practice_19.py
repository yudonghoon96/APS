# 문제
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# 입력예시
# 123

# 출력예시
# 3

#풀이
num = int(input())
cnt = 0

while (num > (10**cnt)):
    cnt += 1

print(cnt)