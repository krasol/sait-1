from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from bot import db
from sql import add, buy, delete

@db.message_handler(Command('add'))
async def add_cmd(message: Message):
    s = ' '.join(message.text.split(' ')[1:])
    await add(s)
    await message.answer('Запись добавлена')

@db.message_handler(Command('delete'))
async def add_cmd(message: Message):
    s = ' '.join(message.text.split(' ')[1:])
    await delete(s)
    await message.answer('Запись успешно удалена')

@db.message_handler(Command('give'))
async def buy_cmd(message: Message):
    await message.answer(await buy())






