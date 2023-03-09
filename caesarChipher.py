alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def decrypt(text, offset):
    result = ''
    text = text.upper()
    for i in text:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto - offset
        if i in alfavit_RU:
            result += alfavit_RU[new_mesto]
        else:
            result += i
    return result

def encrypt(text, offset):
    result = ''
    text = text.upper()
    print(text)
    for i in text:
        mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском 
        new_mesto = mesto + offset
        if i in alfavit_RU:
            result += alfavit_RU[new_mesto]
        else:
            result += i
    return result