n = int(input(''))
def silnia(argument):
    silnia_n = {
    0: '0 1',
    1: '0 1',
    2: '0 2',
    3: '0 6',
    4: '2 4',
    5: '2 0',
    6: '2 0',
    7: '4 0',
    8: '2 0',
    9: '8 0',
    10: '0 0',
    }
    return silnia_n.get(argument, '')

for i in range(n):
    x = int(input(''))
    if (x>10):
        x = 10
    print(silnia(x))
