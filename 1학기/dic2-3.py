#주사위 굴리는 프로그램
import random #임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.

def rolling_dice(pip, repeat):
    for r in range(1, repeat+1):
        n = random.randint(1,pip)
        print(pip,"면 주사위 굴린 결과 ", r," : ", n) #print(str(pip)+"면 주자위 굴린 결과 ", r," : ", n)

rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)