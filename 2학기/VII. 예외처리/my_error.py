#219p

# class MyError(Exception):
#     pass
class OddError(Exception):
    def __init__(self, message="홀수는 ㄴㄴ"):
        self.message = message

    def __str__(self):
        return self.message

n = 9
try:
    if n%2 != 0 :
        raise OddError
    else:
        print(n,", n/2 = ",n/2)
except:
    print("에러발생")