import asyncio
from telethon import TelegramClient, events, Button
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

# библиотека «telethon» - это такая библиотека чтобы управлять аккаунтом через пайтон ток надо создать файл .session а это уже прикол в том что надо войти в аккаунт от лица самой библиотеки

# библиотека аиограм тупо для созданий ботов тг

#всякие айдишники для девов тг 
API_ID = 21311892
API_HASH = 'a67a0cd8341689490ac5104ee83b25ab'
SESSION_NAME = "session"
farmbot = "flamestarsbot"
clickcd = "90"

#токен бота для аиограм
TOKEN = "7227361028:AAGyTH0AhT7iu9fkcuGSJXnkqOrE4pCopQ4"

# кд нажатий
CLICK_INTERVAL = 90

# создание бота и вход сессий
telethon_client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
bot = Bot(token=TOKEN)
dp = Dispatcher()

last_message_id = None
last_chat_id = None

#автоклик
async def auto_click():
    global last_message_id, last_chat_id
    while True:
        if last_message_id and last_chat_id:
            try:
                async with telethon_client as client:
                    await client(GetBotCallbackAnswerRequest(
                        last_chat_id,
                        last_message_id,
                        data="button_callback_data"
                    ))
                    print("Кнопка нажата!")
            except Exception as e:
                print(f"Ошибка при нажатии: {e}")
        await asyncio.sleep(CLICK_INTERVAL)

    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer("ку")


    async def find_last_message():
        global last_message_id
        async with telethon_client:
            async for message in telethon_client.iter_messages(TARGET_BOT_USERNAME, limit=5):
                if message.reply_markup:
                    last_message_id = message.id
                    print(f"Найдено сообщение с кнопкой! ID: {last_message_id}")
                    return
            print("Сообщение с inline-кнопкой не найдено!")

    # Функция для автоматического нажатия кнопки в другом боте
    async def auto_click():
        while True:
            if last_message_id:
                try:
                    async with telethon_client:
                        await telethon_client(GetBotCallbackAnswerRequest(
                            peer=TARGET_BOT_USERNAME,
                            msg_id=last_message_id,
                            data=b"button_callback_data"  # ЗАМЕНИ на реальный callback-код кнопки!
                        ))
                        print("Кнопка нажата в другом боте!")
                except Exception as e:
                    print(f"Ошибка при нажатии: {e}")
            await asyncio.sleep(CLICK_INTERVAL)
    
    async def main() -> None:
        bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        await dp.start_polling(bot)


    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
