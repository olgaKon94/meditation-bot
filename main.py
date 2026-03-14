from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import random
from dotenv import load_dotenv
load_dotenv()
ЦИТАТЫ = [
    "🌸 Покой начинается с тебя. Не снаружи, а внутри.",
    "✨ Каждый вдох — это новое начало.",
    "🌿 Ты не можешь остановить волны, но можешь научиться серфить.",
    "🙏 Настоящий момент — единственное место, где живёт жизнь.",
    "💫 Тишина — это не пустота. Это пространство для чудес.",
    "🌅 Каждое утро — шанс начать всё заново.",
    "🍃 Отпусти то, что не можешь контролировать.",
    "💛 Ты уже достаточно. Прямо сейчас, такой как есть.",
    "🌊 Расслабься. Всё приходит в своё время.",
    "🕊️ Мир внутри тебя сильнее любого шторма снаружи.",
]

МУЗЫКА = [
    ("🌊 Звуки океана", "https://www.youtube.com/watch?v=WHPEKLQID4U"),
    ("🌧️ Звуки дождя", "https://www.youtube.com/watch?v=yIQd2Ya0Ziw"),
    ("🎵 Тибетские поющие чаши", "https://www.youtube.com/watch?v=qk-6_7B5oqo"),
    ("🌿 Звуки природы", "https://www.youtube.com/watch?v=eKFTSSKCzWA"),
    ("🧘 Музыка для медитации", "https://www.youtube.com/watch?v=lFcSrYw-ARY"),
]

МЕДИТАЦИИ = {
    "🌅 Утренняя": """
🌅 *Утренняя медитация (5 минут)*

Сядьте удобно, закройте глаза.
Сделайте 3 глубоких вдоха и выдоха.

Представьте, как утреннее солнце наполняет вас теплом.
С каждым вдохом вы заряжаетесь энергией.
С каждым выдохом уходит всё лишнее.

Побудьте в этом состоянии 5 минут. 🙏
""",
    "🌙 Вечерняя": """
🌙 *Вечерняя медитация (5 минут)*

Лягте или сядьте удобно.
Закройте глаза и расслабьте тело.

Вспомните три хорошие вещи, которые случились сегодня.
Почувствуйте благодарность за прожитый день.
Отпустите всё, что вас беспокоило.

Пусть ночь будет спокойной. 🌙
""",
    "😮‍💨 Дыхание": """
😮‍💨 *Дыхательная практика*

Это упражнение снимает стресс за 3 минуты.

Вдох через нос — считайте до 4
Задержка дыхания — считайте до 4
Выдох через рот — считайте до 8

Повторите 5 раз.
Вы почувствуете спокойствие. ✨
""",
    "🆘 Срочно успокоиться": """
🆘 *Быстрая помощь при тревоге*

Осмотритесь вокруг и назовите:
- 5 вещей, которые вы ВИДИТЕ
- 4 вещи, которые вы можете ПОТРОГАТЬ
- 3 звука, которые вы СЛЫШИТЕ
- 2 запаха, которые вы ЧУВСТВУЕТЕ
- 1 вкус во рту

Это возвращает вас в настоящий момент. 🤍
"""
}

def главное_меню():
    кнопки = [
        ["🌅 Утренняя", "🌙 Вечерняя"],
        ["😮‍💨 Дыхание", "🆘 Срочно успокоиться"],
        ["💬 Цитата дня", "🎵 Музыка"]
    ]
    return ReplyKeyboardMarkup(кнопки, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧘 Привет! Я бот медитаций.\n\nВыберите практику, которая вам нужна прямо сейчас:",
        reply_markup=главное_меню()
    )

async def обработка(update: Update, context: ContextTypes.DEFAULT_TYPE):
    текст = update.message.text

    if текст == "💬 Цитата дня":
        цитата = random.choice(ЦИТАТЫ)
        await update.message.reply_text(цитата, reply_markup=главное_меню())
        return

    if текст == "🎵 Музыка":
        название, ссылка = random.choice(МУЗЫКА)
        await update.message.reply_text(
            f"🎵 {название}\n\nНажмите чтобы слушать:\n{ссылка}\n\nВключите и начните медитацию 🧘",
            reply_markup=главное_меню()
        )
        return

    if текст in МЕДИТАЦИИ:
        await update.message.reply_text(
            МЕДИТАЦИИ[текст],
            parse_mode="Markdown",
            reply_markup=главное_меню()
        )
    else:
        await update.message.reply_text(
            "Выберите практику из меню 👇",
            reply_markup=главное_меню()
        )

if __name__ == "__main__":
    TOKEN = os.getenv("TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, обработка))
    print("✅ Бот запущен! Нажмите Ctrl+C чтобы остановить.")
    app.run_polling()