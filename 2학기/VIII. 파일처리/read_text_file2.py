fi = open("history.ama", "r", encoding="utf8")
sum=0
while True:
    data = fi.readline()
    if not data:
        break
    # print(data ,end ="")
    # 한줄안에서 메뉴,이름, 가격 등등 자르기......
    l=data.split() # 화이트 스페이스 : /t,/n 띄어쓰기 있는걸 다자름
    sum += int(l[1]) #음료의 가격 합계를 구한다.

print("총 금액" + str(sum) + "원")
    # print(l[1])
    #총금액 계산 후 출력하기

fi.close()
