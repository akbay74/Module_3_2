def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        flag_rec = False
        flag_sen = False
        email_end = [".com", ".ru", ".net"]
        for i in email_end:
            if recipient.endswith(i):
                flag_rec = True
                break
        for i in email_end:
            if sender.endswith(i):
                flag_sen = True
                break
        if flag_rec and flag_sen:
           if sender == recipient:
               print("Нельзя отправить письмо самому себе!")
           elif sender == "university.help@gmail.com":
               print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
           else:
               print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
           print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')