if __name__ == '__main__':
    # Весь код, который должен выполниться
    # при запуске из командной строки — тут

    user_info = {"first_name":"", "last_name":""}
    user_info["first_name"] = input ('Введите ваше имя: ')
    user_info["last_name"] = input ('Введите вашу фамилию: ')
    print (user_info)