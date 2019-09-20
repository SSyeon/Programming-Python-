l = [1,2,3]
try:
    print(l[1]) #IndexError: list index out of range
    print(l[2])
except IndexError as e:
    print("인덱스 에러")
    print(e)
else:   #except에 안걸리면 나왔을 텐데....
    print("성공적으로 모든 코드를 실행")