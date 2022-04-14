from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Chooose one", reply_markup=menu)

@dp.message_handler(Text(equals=["Кто они? Дебют"]))
async def get_food(message:Message):
    await message.answer(f"BTS (корейский: 방탄소년단) - мужская группа из семи участников компании BigHit Music. "
                         f"Они дебютировали 13 июня 2013 года с синглом 'No More Dream'. ",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Мемберы"]))
async def get_food(message:Message):
    await message.answer(f"Участники группы:"
                         f"~Ким Нам Джун (он же RM) - Лидер группы, рэпер, автор песен."
                         "Родился в городе Сеуле 12 сентября 1994 года. Высокий и стройный парень. "
                         "~Ким СокДжин (Джин) - Саб-вокалист и лицо группы."
                         "Родился в городе Аньян 4 декабря 1992 года."
                         "~Мин Юнги (Шуга) - Ведущий рэпер."
                         "Юнги родился в городе Тэгу 9 марта 1993 года. "
                         "~Чон Хо Сок (Джей-Хоуп) - Рэпер, саб-вокалист, танцор."
                         "Родился в городе Кванджу 18 февраля 1994 года"
                         "~Пак Чи Мин (Чимин) - Вокалист, танцор. "
                         "Родился в городе Пусане 13 октября 1995 года."
                         "~Ким Тэ Хён (Ви) - Саб-вокал."
                         "Родился в городе Тэгу 30 декабря 1995 года"
                         "~Чон Чонгук (Чонгук) - Рэпер, танцор и вокалист."
                         "Родился в городе Пусане 1 сентября 1997 года.",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Последний альбом"]))
async def get_food(message:Message):
    await message.answer(f"~Butter/Permission to Dance~"
                         "Этот альбом понравился 98 % пользователей"
                         "Исполнитель: BTS"
                         "Дата выпуска: 9 июля 2021 г.",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Награды"]))
async def get_food(message:Message):
    await message.answer(f"Oчееееееееееень, слиииишкооооом много ",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Песни"]))
async def get_food(message:Message):
    await message.answer(f"У бтс очеень много песен и вы точно найдете ту самую."
                         "Перейдите по ссылке)"
                         "https://t.me/bts_music",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Новости"]))
async def get_food(message:Message):
    await message.answer(f"Перейдите по ссылке:3"
                         "https://t.me/btsnews3818",
                         reply_markup=menu)

@dp.message_handler(Text(equals=["Еще"]))
async def get_food(message:Message):
    await message.answer(f"Еще много нового O~0 : https://t.me/bts_files",
                         reply_markup=menu)