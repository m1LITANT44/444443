import random
try:
    syllabus = {
        'Элементы высшей математики': 2,
        'Архитектура аппаратных средств': 2,
        'Основы алгоритмизации и программирования': 3,
        'Основы графики и дизайна': 2,
        'Иностранный язык': 2,
        'Информационные технологии': 1,
        'Базы данных': 3,
        'Физкультура': 3
    }

    while True:
        print('Список возможных действий:')
        print('1 - Вывести "учебный план" на экран ')
        print('2 - Найти информацию по части названия предмета')
        print('3 - Добавить новый предмет в учебный план')
        print('4 - Удалить  предмет из учебного плана')
        print('5 - Изменить  количество часов по предмету')
        print('0 - Закончить работу')
        # запрашиваем у пользователя номер действия:
        user_choice=int(input("Выберите № действия: "))
        if(user_choice==1):
            print("Учебный план:")
            sum=0
            for subject in syllabus:
                hours = syllabus[subject]
                print(f"{subject}: {hours} ч.")
                sum += hours
            print(f'Общее количество занятий по всем предметам: {sum}')
            break
        if(user_choice==2):
            user_input = input('Введите предмет, чтобы вывести информацию о нем')
            print(syllabus.keys())
            for i in syllabus.keys():
                if user_input in i:
                    print('Ура!')
            if user_input not in syllabus.keys():
                print('Такого предмета нет')
            break
        if(user_choice==3):
            input_orig = input('Введите новый предмет:')
            input_hours = int(input('Введите количество часов'))
            if input_orig in syllabus:
                print('Слово уже есть, введите другое название')
            syllabus[input_orig]=input_hours
            print(f'Предмет {input_orig} был добавлен в словарь')
            for subject in syllabus.keys():
                print(f'{subject}: {syllabus[subject]} ч.')
            break
        if(user_choice==4):
            syllabus_delete = input('Введите предмет который хотите удалить:')
            if syllabus_delete not in syllabus:
                print('Такого предмета нет!')
            else:
                del syllabus[syllabus_delete]
                for key, value in syllabus.items():
                    print(key, value)
            break
        if(user_choice==5):
            input_syllabus_hour = input('Введите предмет, часы которого вы хотите изменить ')
            if input_syllabus_hour not in syllabus:
                print('Такого предмета нет!')
            else:
                input_hour = int(input('Введите количество часов'))
                syllabus[input_syllabus_hour] = input_hour
                for key, value in syllabus.items():
                    print(key, value)
            break
        if(user_choice==0):
            print('До свидания!')
            break

except ValueError as e:
    print("Не правильный ввод данных")