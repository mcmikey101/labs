import random

def toCaps(text):
    try:
        newText = ''
        alph = 'qwertyuiopasdfghjklzxcvbnm'
        for i in text:
            if i in alph:
                newText += chr(ord(i) - 32)
            else:
                newText += i
        return newText
    except:
        return 'Что-то не так'
    
def scramble(text):
    try:
        newText = ''
        arr = list(text)
        for i in range(len(arr)):
            char = random.choice(arr)
            newText += char
            arr.remove(char)
        return newText
    except:
        return 'Что-то не то'