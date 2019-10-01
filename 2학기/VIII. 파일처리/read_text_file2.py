fi = open("history.ama", "r", encoding="utf8")

while True:
    data = fi.readline()
    if not data:
        break
    print(data ,end ="")
    # 한줄안에서 메뉴,이름, 가격 등등 자르기......
    #총금액 계산 후 출력하기

fi.close()

