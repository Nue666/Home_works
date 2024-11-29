def send_email(message, recipient, sender = "university.help@gmail.com"):
    valid_endings = ('.com', '.ru', 'net')
    if '@' in recipient and '@' in sender and recipient.endswith(valid_endings) and sender.endswith(valid_endings):
        if recipient != sender:
            if sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print('Нельзя отправить письмо самому себе!')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print()
message, sender, recipient = input('Введите ваше сообщение: '),input('Введите свой адрес эл.почты: '),input('Введите адрес получателя:')
print()
send_email(message,sender,recipient)