'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
'''


def modify_data(data, keyword):
    results = []
    for entry in data:
        for value in entry:
            if keyword.lower() in value.lower():
                results.append(entry)
                break
    if not results:
        print("Записи не найдены.")
    else:
        print("Результаты поиска:")
        print_data(results)
        choice = input("Введите номер записи, которую хотите изменить или удалить: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(results):
                action = input("Выберите действие (1 - изменить, 2 - удалить): ")
                if action == "1":
                    print("Изменение записи:")
                    new_entry = []
                    new_entry.append(input("Введите фамилию: "))
                    new_entry.append(input("Введите имя: "))
                    new_entry.append(input("Введите отчество: "))
                    new_entry.append(input("Введите номер телефона: "))
                    results[index] = new_entry
                    print("Запись успешно изменена.")
                elif action == "2":
                    del data[data.index(results[index])]
                    print("Запись успешно удалена.")
                else:
                    print("Некорректный ввод.")
            else:
                print("Некорректный номер записи.")
        else:
            print("Некорректный ввод.")
