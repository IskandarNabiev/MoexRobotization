#С использованием библиотеки
from itertools import groupby

def encoder(text):
    encoded_text = ''
    # Группировка элементов по значению
    for key, group in groupby(text):
        count = len(list(group))
        if count > 1:
            encoded_text += str(count) + key
        else:
            encoded_text += key
    return encoded_text

print(encoder("aaaaBBbbCooa"))


# Без использования библиотек
def encoder(text):
    encoded_text = ''
    prev_char = ''
    count = 1

    if not text:
        return ''

    for char in text:
        # Если предыдущий и текущий символы не совпадают
        if char != prev_char:
            # Добавить количество и символ в encoded_text
            if prev_char:
                encoded_text += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Увеличить счетчик, если символы совпадают
            count += 1
    else:
        encoded_text += str(count) + prev_char
        #Число символа в единственном количестве убирается
        return encoded_text.replace('1', "")

example = encoder("aaaaBBbbCooa")
print(example)

