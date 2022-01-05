from telegram.ext import Updater, CommandHandler, MessageHandler , Filters
from telegram import  ReplyKeyboardMarkup

hafta_kunlari=ReplyKeyboardMarkup([
    ["Dushanba","Seshanba"],
    ["Chorshanba","Payshanba"],
    ["Juma","Shanba"],
    ["Yakshanba"]

])









def start(update,context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Salom  @{user.username},  Dars jadvalga hush kelibsiz! ",reply_markup=hafta_kunlari)



def xabar(update,context):
    hafta_kunlari=update.message.text
    if hafta_kunlari=="Dushanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Dushanba:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari=="Seshanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Seshanba:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari=="Chorshanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Chorshanba:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari=="Payshanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Payshanba:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari=="Juma":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Juma:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari=="Shanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Shanba:\nJismoniy-tarbiya \nona tili \nGeografiya \nTarbiya \nIngiliz tili \ndarslari bor")
    elif hafta_kunlari == "Yakshanba":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Bugun Yakshanba:bugun dam olish kun!")


updater=Updater(token="5007298866:AAEfIs3aD5NctUEGVp8QKIOLMwLJgGH0ChA", use_context=True)
dispatcher=updater.dispatcher



start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,xabar)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)



updater.start_polling()
print("hammasi yaxshi")
















