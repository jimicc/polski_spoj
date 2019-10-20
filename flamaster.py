c  = int(input(''))
for i in range(c):
    word = ''
    count = 1
    text = input('')
    text += ' '
    length = len(text)
    for i in range(length -1):
        if (text[i] == text[i+1]):
            count += 1
        else:
            if (count > 2):
                word += text[i]
                word += str(count)
                count = 1
            elif (count == 2):
                word += text[i]
                word += text[i]
                count = 1
            else:
                word += text[i]
    print(word)


