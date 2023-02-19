from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варинта: "))

    while var != 1 and var != 2:
        var = int(input(" : "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!')




    



def print_data():
    print('1 Файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_second.append(''.join(data_first[j:i]))
                j = i
        data_first = data_first_second
        print(''.join(data_first))



    print('2 Файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())

        print(*data_second)
    
    return data_first, data_second




def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        
        while number_journal < 1 or number_journal > 4 :
            print('Ты дурак?! Даю тебе последний шанс')
            number_journal = int(input('Введите номер записи: '))

        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = adress_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        
        while number_journal <=0 or number_journal > 4 :
            print('Ты дурак?! Даю тебе последний шанс')
            number_journal = int(input('Введите номер записи: '))
         
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = adress_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!\n')  
    print_data() 




def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        
        while number_journal < 0 or number_journal > 4 :
            print('Ты дурак?! Даю тебе последний шанс')
            number_journal = int(input('Введите номер записи: '))

        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        
        while number_journal < 0 or number_journal > 4 :
            print('Ты дурак?! Даю тебе последний шанс')
            number_journal = int(input('Введите номер записи: '))

        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!\n')
    print_data() 