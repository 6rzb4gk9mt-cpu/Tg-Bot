from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставь сюда токен от @BotFather
BOT_TOKEN = "8659628092:AAEgRemLtETYxBtPQlw_24GhR8sRpfPddTw"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Доступные команды:\n"
        "/contact — написать нам\n"
        "/idea — рассказать нам о своей идее"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /contact — показывает контакты"""
    await update.message.reply_text(
        "📬 Наши контакты:\n\n"
        "• @obsidier\n"
        "• @Timmy_Falcon\n\n"
        "Напишите нам — мы всегда рады! 😊"
    )


async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /idea — пересылает идею пользователя в @obsidier"""
    # Проверяем, есть ли текст после команды
    if context.args:
        idea_text = " ".join(context.args)
        sender = update.message.from_user

        # Формируем имя отправителя
        if sender.username:
            sender_name = f"@{sender.username}"
        else:
            full_name = sender.full_name or "Неизвестный"
            sender_name = f"{full_name} (id: {sender.id})"

        # Отправляем идею в личку @obsidier
        try:
            await context.bot.send_message(
                chat_id="@obsidier",
                text=(
                    f"💡 Новая идея!\n\n"
                    f"От: {sender_name}\n\n"
                    f"Идея:\n{idea_text}"
                )
            )
            await update.message.reply_text(
                "✅ Спасибо! Твоя идея отправлена. Мы обязательно её рассмотрим! 🙌"
            )
        except Exception as e:
            await update.message.reply_text(
                "⚠️ Не удалось отправить идею. Попробуй написать напрямую: @obsidier"
            )
            print(f"Ошибка отправки: {e}")
    else:
        await update.message.reply_text(
            "📝 Напиши свою идею после команды!\n\n"
            "Пример:\n"
            "/idea Хочу предложить новую функцию..."
        )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("idea", idea))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
