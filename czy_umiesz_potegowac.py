wyk = {1: "1111", 2: "2486", 3: "3971", 4: "4646", 5: "5555", 6: "6666", 7: "7931", 8: "8426", 9: "9191", 0: "0000"}
p = int(input(""))
for i in range(p):
    d = input("")
    podstawa = int(d[d.find(" ")-1])
    potega = int(d[d.find(" "):]) % 4
    text = wyk[podstawa]
    if (int(d[-1]) == 0):
        print(int('1'))
    else:
        print(int(text[potega-1]))