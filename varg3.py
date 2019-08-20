def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)
p(",", 3, "ㄱ", "ㄴ")
p("ㅇ", 2, "ㄱ", "ㄴ", "ㄷ")
p("_", 3, "ㄱ", "ㄴ", "ㄷ", "ㄹ")