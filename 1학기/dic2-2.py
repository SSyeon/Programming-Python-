#주사위 굴리는 프로그램
import random #임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.

def rolling_dice(pip):
    n = random.randint(1,pip)
    print(pip,"면 주사위 굴린 결과 : ", n) #print(str(pip)+"면 주자위 굴린 결과 : ", n)

rolling_dice(4)
rolling_dice(6)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(20)