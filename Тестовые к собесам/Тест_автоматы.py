import random
# Обычные символы 1, 2, 3, 4, 5, 6, 7, 8
# Wild символ - 0
# Символ Free Spins - 9
reels = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

reels_free = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

def spin(free):
    spinResult=[[0,0,0], [0,0,0],[0,0,0]]
    if free == 0:
        for reel in reels:
            for i in range(3):
                for j in range(3):
                    spinResult[i][j]=random.choice(reel)
    return spinResult

# for i in range(1000):
#     currSpin = spin(0)
#     if currSpin == '777':
#         print("You win")
print(spin(0))