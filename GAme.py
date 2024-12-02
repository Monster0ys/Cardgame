from random import randrange

colors = ["Red", "Green", "Blue", "Yellow"]
arr=[]
for color in colors:    
    for num in range(10):
        arr.append(f"{num} {color}")
        arr.append(f"{num} {color}")

def shuffle_array(arr):
    for i in range(len(arr) -1,0,-1): # Идем с конца массива
        j = randrange(i+1)            # Выбираем случайный индекс от 0 до i включительно
        arr[i], arr[j]=arr[j], arr[i] # Меняем местами элементы

shuffle_array(arr)

print('\n'.join(arr))

   
