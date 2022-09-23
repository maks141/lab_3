string = input('Шифр цезаря. Введите на английском строку, которую хотите зашифровать/расшифровать: ')
quest = input('Хотите зашифровать или дешифровать? (введите 1 или 2): ')
step = int(input('Введите шаг сдвига: '))

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_abc = abc

# Создаем новый алфавит по сдвигу
for i in range(0, step):
    new_abc.append(abc[i])
new_abc = new_abc[i+1::]

# Создаем шифрованную/дешифрованную строку
def MakeNewString():
    new_string = ''
    if quest == '1':
        for i in string:
            if i != ' ':
                new_string += new_abc[abc.index(i)]
            else:
                new_string += ' '
        return new_string
    elif quest == '2':
        for i in string:
            if i != ' ':
                new_string += abc[new_abc.index(i)]
            else:
                new_string += ' '
        return new_string


print(MakeNewString())
