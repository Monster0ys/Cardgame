from random import randrange

colors = ["Red", "Green", "Blue", "Yellow"]
arr=[]
for color in colors:    
    for num in range(10):
        arr.append(f"{num} {color}")
        arr.append(f"{num} {color}")

def shuffle_array(arr):
    for i in range(len(arr) -1,0,-1):   # Идем с конца массива
        j = randrange(i+1)              # Выбираем случайный индекс от 0 до i включительно
        arr[i], arr[j] = arr[j], arr[i] # Меняем местами элементы

shuffle_array(arr)

num_players = int(input("Введите количество игроков: "))
num_of_card = int(input("Введите количество карт на игрока: "))

if num_players * num_of_card +1 <= len(arr):
    card_on_table = arr.pop()                               #Карта на столе

    print("\nКарты на руках у игроков")
    
    for player_number in range(1,num_players+1):            #Номер игрока
        hand=[]                                             #Карты каждого игрока
        for _ in range(num_of_card):                        #Подчеркивание '_' используется вместо имени переменной, так как значение итерации не используется.
            hand.append(arr.pop())                          #Добавление карты в руку
        print(f"Игрок {player_number}: {', '.join(hand)}")

    print(f"\nКарта на столе: {card_on_table}")

else:print("В колоде недостаточно карт для игры!")

   
