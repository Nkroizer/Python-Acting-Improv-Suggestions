import random

array = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44]
random.shuffle(array)
start = 0
end = 4
for i in range(4):
    print(array[start:end])
    start += 4
    end += 4
