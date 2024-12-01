colors = ["Red", "Green", "Blue", "Yellow"]
arr=[]
for color in colors:    
    for num in range(10):
        arr.append(f"{num} {color}")
        arr.append(f"{num} {color}")
print('\n'.join(arr))

   
