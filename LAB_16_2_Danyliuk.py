path = 'C:/Users/danil/Desktop/ICS6/Laboration#16/numbers.txt'

with open (path , 'r') as file:
    text = file.read().split(",") # зчитує наш файл та розділяє по комам
count = {}

for num in text:
    num = int(num) # зазначаємо що там лише цілі числа
    if num in count:
        count[num] += 1 # якщо зустрічає число тоді до словника додається +1 {'10' : 1+1+... , ...}
    else:
        count[num] = 1 # якщо ж не зустрічається =1 {'11' : 1 , ...}

x = list(count.keys()) # рахує ключі "10" чи "11"
y = list(count.values()) # рахує відповідності :1 чи :2 . Це та сама кількість

#-------------------------------------------------------------------------------------#

import matplotlib.pyplot as plt

plt.bar(x,y)
plt.xticks(x) # показує лише ті числа , що є у списку
plt.xlabel("NUMBERS")
plt.ylabel("COUNTINGS")
plt.title("Gistogram of Countings of Numbers")

plt.show()