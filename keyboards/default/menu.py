from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кто они? Дебют"),
            KeyboardButton(text="Мемберы"),
        ],
        [
            KeyboardButton(text="Последний альбом"),
            KeyboardButton(text="Награды"),
        ],
        [
            KeyboardButton(text="Песни"),
            KeyboardButton(text="Новости"),
        ],
        [
            KeyboardButton(text="Еще"),
        ],
    ],
    resize_keyboard=True
);