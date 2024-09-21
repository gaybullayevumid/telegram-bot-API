# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
# from telegram import ReplyKeyboardMarkup, KeyboardButton
# from telegram.ext import filters

# TOKEN = '7714575462:AAE88sVMe9_NsfZ1fBSEeOjqCSy1iOe2Lwo'

# async def start(update, context):
#     await update.message.reply_text("Salom! Ma'lumotlaringizni olish uchun /getinfo yozing.")

# async def get_user_info(update, context):
#     user_id = update.message.from_user.id
#     username = update.message.from_user.username
#     await update.message.reply_text(f"ID: {user_id}\nUsername: @{username}")

# async def request_phone_number(update, context):
#     button = KeyboardButton(text="Telefon raqamni ulashish", request_contact=True)
#     reply_markup = ReplyKeyboardMarkup([[button]], one_time_keyboard=True)
#     await update.message.reply_text("Telefon raqamingizni yuboring:", reply_markup=reply_markup)

# async def handle_phone_number(update, context):
#     # contact'ni update.message.contact orqali olish
#     contact = update.message.contact
#     if contact:
#         phone_number = contact.phone_number
#         await update.message.reply_text(f"Telefon raqam: {phone_number}")
#     else:
#         await update.message.reply_text("Telefon raqamni olishda xatolik.")

# async def get_profile_image(update, context):
#     user_id = update.message.from_user.id
#     photos = await context.bot.get_user_profile_photos(user_id)
#     if photos.total_count > 0:
#         photo_file_id = photos.photos[0][-1].file_id
#         await update.message.reply_photo(photo=photo_file_id)
#     else:
#         await update.message.reply_text("Profil rasm mavjud emas.")

# async def main():
#     application = ApplicationBuilder().token(TOKEN).build()

#     # Qo'llanadigan handlerlarni qo'shish
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("getinfo", get_user_info))
#     application.add_handler(CommandHandler("getphoto", get_profile_image))
#     application.add_handler(CommandHandler("getphone", request_phone_number))
#     application.add_handler(MessageHandler(filters.CONTACT, handle_phone_number))

#     # Botni to'g'ri boshlash uchun avval initialize() chaqiramiz
#     application.initialize()

#     # Botni ishga tushirish
#     application.run_polling()

# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())

