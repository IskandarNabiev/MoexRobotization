
# 1й способ
from random import random

# 1000 случайных чисел
N = 1000
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 1000)
print(arr)

def most_frequent(data):
    counter = 0
    num = data[0]

    for i in data:
        curr_freq = data.count(i)
        if (curr_freq > counter):
            counter = curr_freq
            num = i

    print("Наиболее встречающееся число: {}, встречается {} раз(а)".format(num, counter))

most_frequent(arr)


# 2й способ
from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
most_freq = 1
for i in range(N - 1):
    freq = 1
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            freq += 1
    if freq > most_freq:
        most_freq = freq
        num = arr[i]

if most_freq > 1:
    print(most_freq, 'раз(а) встречается число', num)
else:
    print('Уникальные элементы')

