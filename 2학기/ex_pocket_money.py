# 국어,영어, 수학, 자바, 파이썬, JSP
# 총점 , 평균 구하기
# 용돈 구하기
# 90점 이상 100,000원
# 80점 이상 80,000원
# 70점 이상 70,000원
# 60점 이상 60,000원
# 그 미만 50,000원
from typing import List, Union

# subject= ["국어","영어","수학","자바","파이썬","JSP"]
# score =[0,0,0,0,0,0]
# for i in range(0,5+1):
#   score[i]=input(subject[i]+"점수를 입력해 주세요")
#   print(subject[i]+"는 : "+ score[i])
#
# for i in score:
#     sum_score=0
#     sum_score += int(score[i])
#     print(sum_score)

k = input("국어 점수는?")
e = input("영어 점수는?")
m = input("수학 점수는?")
j = input("자바 점수는?")
p = input("파이썬 점수는?")
jsp = input("JSP 점수는?")

sum = int(k) + int(m) + int(e) + int(j) + int(p) + int(jsp)
print("총점은", sum)
avg = sum / 6
print("평균은",round(avg,2))

if avg>=90:
    print("용돈 100,000원")
elif avg>=80:
    print("용돈 80,000원")
elif avg>=70:
    print("용돈 70,000원")
elif avg>=60:
    print("용돈 60,000원")
else:
    print("용돈 50,000원")