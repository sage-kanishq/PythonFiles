height = int(input())
height2 = height
for i in range(height2):
    print(f'{" "*(height-1)}{"#"*(i+1)}')
    height-=1