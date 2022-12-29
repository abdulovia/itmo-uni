logins = ['abe', 'itmo', 'admin', 'super user', 'wines']
log_input = input('Логин: ')
if log_input in logins:
    print('Доступ разрешён')
else:
    print('Вы хотите создать новый логин?')
    answer = input() # Да/Нет
    if answer == 'Да':
        login = input('Введите логин: ')
        logins.append(login)
        print('Логин успешно добавлен!')
        print(*logins)
    else:
        print('Доступ запрещен!')
    
    