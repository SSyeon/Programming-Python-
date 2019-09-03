# **
import random

print("0 이상 1 미만 실수 값")
print("random.random() : ", random.random())
print()
print("시작값 2.5 이상 끝값 10.0 미만 실수 값")
print("random.uniform(2.5, 10.0) : ", random.uniform(2.5, 10.0))
print()
print("100이상 999이하 정수 값")
print("random.randint(100,999) : ", random.randint(100,999)) #끝수가 포함됨
print()
print("0 이상 끝값 10 미만 정수 값")
print("random.randrange(10) : ", random.randrange(10)) #끝수 안포함
print()
print("1 이상 끝값 7 미만, 증가 값이 2인 정수 값")
print("random.randrange(1, 7, 2) : ", random.randrange(1, 7, 2))
print()
print("리스트에서 1개 값 꺼내오기")
season = ["봄", "여름", "가을", "겨울"]
print("season = ", season)
print("random.choice(season) : ", random.choice(season))#중복이 생길 수 있음
print()
l = ["가", "나", "다", "라", "마"]
print("리스트 순서를 섞기")
print("섞기 전 l = ", l)
random.shuffle(l)
print("random.shuffle(l)") #중복없음
print("섞은 후 l = ", l)
print()
print("리스트에서 몇 개의 값을 중복하지 않고 3개 뽑기")
sample = ["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번", "9번"]
print("샘플대상 = ", sample)
print("random.sample(sample, 3) : ", random.sample(sample, 3))
#초이스랑 셔플이 짬뽕댐!