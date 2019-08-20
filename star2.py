def star(mark, *args):
    for a in args:
        print(mark*a)
        
star("ㄱ", 3)
star("ㄴ", 1, 2, 3)