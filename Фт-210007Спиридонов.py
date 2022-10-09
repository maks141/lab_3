abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    input_string = input('Шифр цезаря. Введите на английском строку, которую хотите зашифровать/расшифровать: ')
    c = 0
    for i in input_string.lower():
        if i in abc:
            c += 1
        else:
            print('Введите строку на англиском языке!')
            break
    if len(input_string) == c:
        break

while True:
    quest = input('Хотите зашифровать или дешифровать? (введите 1 или 2): ')
    if quest == '1' or quest == '2':
        break
    else:
        print('Введите 1 или 2!')

while True:
    step = int(input('Введите шаг сдвига: '))
    if step <= 0:
        print('Введите положительный шаг сдвига!')
    else:
        break

string = input_string.lower()

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

string_out = []
for i in MakeNewString():
    string_out.append(i)


for i in input_string:
    if i.isupper():
        string_out[input_string.index(i)] = string_out[input_string.index(i)].upper()


print(''.join(string_out))
