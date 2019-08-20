def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("ㄱ")
p("ㄱ", "ㄴ")
p("ㄱ", "ㄴ", "ㄷ", "ㄹ")