# 문제
# 두 수를 Input으로 받아 합을 구하는 코드이다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# numbers = input().split()
# print(sum(numbers))

# 입력예시
# 10 20

# 출력예시
# 30

# 풀이
#sum 에는 int 형 혹은 str 형이 와야한다.
numbers = input().split()

sum_numbers = 0

for i in numbers:
    i = int(i)
    sum_numbers += i
    
print(sum_numbers)