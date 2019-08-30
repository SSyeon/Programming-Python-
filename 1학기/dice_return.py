import random
def dice(pip):
    result = random.randint(1, pip)
    return result

print("6면 주사위의 값은 :", dice(6))