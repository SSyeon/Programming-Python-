def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    return min, max

print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최젓값 :", min_value)
print("최댓값 :", max_value)