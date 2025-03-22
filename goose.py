# DECODED BY HYPER X SQUAD >>> TOP 1 
# @decoded_softs

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import string
import requests
import colored
import json
from colorama import init
init()
from colorama import Fore, Back, Style
from pystyle import *


banner = """                                                                                                                                                                         
"""

text = """  
  ▄██████▄   ▄██████▄   ▄██████▄     ▄████████    ▄████████         ▄████████ ███▄▄▄▄    ▄██████▄     ▄████████ 
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███        ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ 
  ███    █▀  ███    ███ ███    ███   ███    █▀    ███    █▀         ███    █▀  ███   ███ ███    ███   ███    █▀  
 ▄███        ███    ███ ███    ███   ███         ▄███▄▄▄            ███        ███   ███ ███    ███   ███        
▀▀███ ████▄  ███    ███ ███    ███ ▀███████████ ▀▀███▀▀▀          ▀███████████ ███   ███ ███    ███ ▀███████████ 
  ███    ███ ███    ███ ███    ███          ███   ███    █▄                ███ ███   ███ ███    ███          ███ 
  ███    ███ ███    ███ ███    ███    ▄█    ███   ███    ███         ▄█    ███ ███   ███ ███    ███    ▄█    ███ 
  ████████▀   ▀██████▀   ▀██████▀   ▄████████▀    ██████████       ▄████████▀   ▀█   █▀   ▀██████▀   ▄████████▀  
                                                                                                                 
                                                  REALESE V2
                                      ╔══════                      ══════╗
                                      ║     CREATOR - DAYN     ║
                                      ║        VERSION - 2.0.1           ║
                                      ║           PRICE - FREE           ║
                                      ║         LEVER - PREMUIM          ║
                                       ══════════════════════════════════
                                                
                    ╔                          ╗              ╔                          ╗
                      | - 1. снос аккаунта - |                   | - 2. снос канала - | 
                    ╚                          ╝              ╚                          ╝
                     
                    ╔                          ╗              ╔                          ╗
                        | - 3. снос бота - |                    | - 4.  свой текст  - |
                    ╚                          ╝              ╚                          ╝

                    ╔                          ╗              ╔                          ╗
                         | - 5. SOON...   - |                      | - 6. SOON...  - |
                    ╚                          ╝              ╚                          ╝
                   
"""


print()
print(Colorate.Vertical(Colors.blue_to_red, Center.XCenter(banner)))
print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(text)))



COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

senders = {
"figoovdxjn@rambler.ru": "5907967vN2Smd",
"qxoqdttfrw@rambler.ru": "7532241lJmL4W",
"qkejvgpvpp@rambler.ru": "5398970avTpP4",
"yujnpwzbfa@rambler.ru": "8852257OSqIDV",
"jxkdemjgde@rambler.ru": "2125065SlSfbE",
"hlssjwnime@rambler.ru": "82126976rz3WJ",
"vzawnrrkgj@rambler.ru": "1034318ijbNEu",
"wxdblhfcdj@rambler.ru": "8945966PQNRJo",
"yszicfwxmi@rambler.ru": "8860786p7sw4K",
"dchxatnyqr@rambler.ru": "4380737WmI2aJ",
"fccrbvtebj@rambler.ru": "7532241lJmL4W",
"hypyfnqbvc@rambler.ru": "8584985xbLVuy",
"nleqavwdss@rambler.ru": "1635937Bhth8G",
"jxqrxbcgch@rambler.ru": "37175383PcV1l",
"mfkfpxhwvc@rambler.ru": "2853634MCe0Qw",
"ieovzgvnds@rambler.ru": "4130435ASTfYb",
"nkonrpmpoo@rambler.ru": "72950941eygG3",
"uyioldixre@rambler.ru": "6030225uK4a7S",
"dtnycnyoqh@rambler.ru": "5001142Toimr4",
"ppiuxvldrl@rambler.ru": "5773527PXyiTk",
"jypwndnboa@rambler.ru": "8883382tktBVE",
"rjqczegnet@rambler.ru": "7789265B8SAtf",
"gabcbfqetv@rambler.ru": "9662775l5lPkB",
"llzqpbhsrm@rambler.ru": "0478587jtSHBa",
"ldwdizfync@rambler.ru": "9995714DnwZjT",
"vjxvmxaedl@rambler.ru": "97387528ygyG8",
"mslpuyozgb@rambler.ru": "9218853iuUYjQ",
"osrhgmkxgu@rambler.ru": "1115575ZWbvt0",
"kdharmmuyy@rambler.ru": "9128380AZgtWQ",
"dlljoohamr@rambler.ru": "6500979b36HIX",
"gzkyzbkupg@rambler.ru": "7735702Thx0kv",
"dmtjsviosp@rambler.ru": "4773490tY4qNn",
"mmvqrthflf@rambler.ru": "8505788cPQ0TO",
"rmamfrismb@rambler.ru": "0426392NcGerk",
"hrjvjcymjb@rambler.ru": "4407212zP5EpL",
"hqyuuhiner@rambler.ru": "13746124rH7oc",
"kuatwwbkmp@rambler.ru": "2912459zay6O1",
"zjnhwoktmm@rambler.ru": "6001714XRpwAn",
"nvbmxdidbp@rambler.ru": "949553969XvZC",
"kkzqdhwzmf@rambler.ru": "397683714XmlX",
"zyugobyttn@rambler.ru": "1215285j9zZVU",
"molrcznpot@rambler.ru": "1995458G3jrd9",
"ahmhpmcuyj@rambler.ru": "0170766RFareq",
"cejabfyjhf@rambler.ru": "4893053ZxXt54",
"eftlqkfoks@rambler.ru": "3627078YQBl27",
"bqnljrnrpp@rambler.ru": "305845036pByj"

}

receivers = ['stopca@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'sticker@telegram.org', 'support@telegram.org', 'security@telegram.org', 'sms@telegram.org', 'info@telegram.org', 'org', 'spam@telegram.org',]


def menu():
    choice = input(f'{COLOR_CODE["PINK"]} Выбери пункт ➤ {COLOR_CODE["RED"]} ')
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server = smtplib.SMTP('smtp.rambler.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(0.5)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = menu()
    if choice == '1':
        print("1. Спам.")
        print("2. Доксинг.")
        print("3. Троллинг.")
        print("5. С вирт номером.")
        print("6. С премиумом.")
        comp_choice = input("-> ")
        if comp_choice in ["1", "2", "3"]:
            print("следуй за указаниям.")
            username = input("юзернейм: ")
            id = input("айди: ")
            chat_link = input("ссылка на чат: ")
            violation_link = input("ссылка на нарушение: ")
            print("Начинаю отправлять жалобы...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я недавно столкнулся с пользователем, который, как мне кажется, занимается массовой рассылкой спама. Его юзернейм - {username}, его айди - {id}, ссылка на чат, где я это наблюдал, - {chat_link}, а вот ссылка на примеры нарушений - {violation_link}. Я бы очень просил вас разобраться с этим случаем и принять необходимые меры в отношении данного пользователя.",
                "2": f"Уважаемая поддержка, на вашей платформе я обнаружил пользователя, который, судя по всему, занимается распространением чужих личных данных без согласия владельцев. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это заметил, - {chat_link}, а вот ссылка на примеры таких нарушений - {violation_link}. Я прошу вас тщательно разобраться в этом инциденте и предпринять соответствующие меры, вплоть до блокировки аккаунта этого пользователя.",
                "3": f"Добрый день, уважаемая поддержка Telegram. Недавно мне довелось наблюдать, как один из пользователей вашей платформы активно использует нецензурную лексику и занимается спамом в чатах. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это видел, - {chat_link}, а вот примеры таких нарушений - {violation_link}. Я очень рассчитываю, что вы отреагируете на этот случай и примете надлежащие меры, включая возможную блокировку аккаунта данного пользователя."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    try:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                        violation_link=violation_link.strip())
                        send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                    except Exception as e:
                        print("Письмо отправленно")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуйте указаниям:")
            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день, поддержка Telegram! Я хотел бы сообщить вам, что пользователь с аккаунтом {username} ({id}) использует виртуальный номер, приобретенный на специализированном сайте по активации номеров. Насколько я могу судить, этот номер не имеет к нему никакого отношения. Я очень прошу вас разобраться в этой ситуации. Заранее благодарю за содействие!",
                "6": f"Уважаемая поддержка Telegram! Мне стало известно, что пользователь с аккаунтом {username} ({id}) приобрел премиум-аккаунт в вашем мессенджере с целью рассылки спам-сообщений и обхода ограничений Telegram. Я настоятельно прошу вас проверить эту информацию и принять необходимые меры. Заранее признателен за ваше внимание к данному вопросу."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Письмо отправленно")
                        time.sleep(5)



    elif choice == "2":
        
        print("1. Докс")
        print("2. Живодёрство")
        print("3. Детское")
        print("4. Прайс")
        ch_choice = input("выбор: ")
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("Осталось совсем чучуть.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(0.5)


    elif choice == "3":
        print("1. Осинт")
        print("2. Наркошоп")
        bot_ch = input("Выберите вариант -> ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("Ожидайте...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "2" :f"Здравствуйте, в вашем мессенджере я наткнулся на бота который производит незаконную торговлю наркотиками. Прошу отреагировать на мою жалобу и принять меры по блокировке данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Письмо отправленно")
                        time.sleep(5)
    elif choice == "5":
        print("хуесос тебе сказали скоро")
        
    elif choice == "6":
        print("хуесос тебе сказали скоро")
    
    elif choice == "7":
        exit
        
        

  
if __name__ == "__main__":
    main()
