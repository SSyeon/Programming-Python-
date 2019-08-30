#주사위 굴리는 프로그램
import random #임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.

def rolling_dice():
    n = random.randint(1,6)
    print("6면 주사위 굴린 결과 : ", n)
rolling_dice()
rolling_dice()