import math
t = int(input(''))
for i in range (t):
    n = int(input(''))
    y = math.floor(math.sqrt(n))
    if (n == 1):
        print('NIE')
    elif (n == 2) or (n == 3):
        print('TAK')
    else:
        for i in range(2,y+1,1):
            if (n % i) ==  0:
                print('NIE')
                break
        else:
            print('TAK')

