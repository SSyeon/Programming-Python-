#star 함수 정의
def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        str = (mark * repeat)
        for j in range(2, repeat):
            str = str+ (space * space_repeat) + (mark * repeat)
        print(str)    

star("※", 3, "_", 2,4)
star(mark = "※", repeat = 3, space = "_", space_repeat=2, line = 4)