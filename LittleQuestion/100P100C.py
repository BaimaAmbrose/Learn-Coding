'''
A rooster costs 5 yuan, a hen costs 3 yuan, and three chicks cost 1 yuan.
Using exactly 100 yuan, buy exactly 100 chickens.
How many roosters, hens, and chicks should you buy?
'''

for i in range(100):
    for j in range(100):
        for z in range(100):
            if z % 3 == 0 and 5 * i + 3 * j + z / 3 == 100 and i + j + z == 100:
                print(f'rooster has {i},hen has {j},chicks have {z}')
