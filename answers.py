chat ={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
def get_answer (key,chat):
	return chat.get(key.lower(), "я тебя не понял")


if __name__ == '__main__':
    # Весь код, который должен выполниться
    # при запуске из командной строки — тут

	key = input ("поговорим?\n")
	result = get_answer(key, chat)
	print (result)

