from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup
import json

def back():
    return [
        [
            InlineKeyboardButton("Orqaga", callback_data='10')
        ]
    ]

def city():
    return [
            [ 
            InlineKeyboardButton("Urgench", callback_data = '1'),
            InlineKeyboardButton("Toshkent", callback_data = '2'),
            ],
            [ 
            InlineKeyboardButton("Samarqand", callback_data = '3'),
            InlineKeyboardButton("Farg`ona", callback_data = '4'),
            ],
            [ 
            InlineKeyboardButton("Jizzax", callback_data = '5'),
            InlineKeyboardButton("Namangan", callback_data = '6'),
            ],
            [ 
            InlineKeyboardButton("Buxaro", callback_data = '7'),
            InlineKeyboardButton("Navoiy", callback_data = '8'),
            ]
        ]



def inline_hendlers(update, context):
    
    
    query = update.callback_query
    query.answer()
    if query.data == '10':
        query.message.edit_text("Ob-havoni bilish uchun bosing 👇",
        reply_markup=InlineKeyboardMarkup(city()) )


    if query.data == '1':
        url = f"https://sinoptik.ua/погода-ургенч"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Urganch ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

    if query.data == '2':
        url = f"https://sinoptik.ua/погода-ташкент"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Toshkent ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )
    
    if query.data == '3':
        url = f"https://sinoptik.ua/погода-самарканд"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Samarqand ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )
    
    if query.data == '4':
        url = f"https://sinoptik.ua/погода-фергана"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Farg`ona ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

    if query.data == '5':
        url = f"https://sinoptik.ua/погода-джизак"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Jizzax ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

    if query.data == '6':
        url = f"https://sinoptik.ua/погода-наманган"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Namangan ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

    if query.data == '7':
        url = f"https://sinoptik.ua/погода-бухара"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Buxoro ob-havo ma`lumoti: \n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

    if query.data == '8':
        url = f"https://sinoptik.ua/погода-навои"
        html_par = requests.get(url).text
        html_par1 = BeautifulSoup(html_par , 'lxml')
        texts = html_par1.find("div", {"id": "bd1"}).text
        query.message.edit_text(f"Navoiy ob-havo ma`lumoti:\n{texts}", 
        reply_markup=InlineKeyboardMarkup(back()) )

def start(update, context):
    user = update.message.from_user
    update.message.reply_html(f"Salom <b>{user.first_name} {user.last_name}</b> \nOb-havoni bilish uchun bosing 👇", 
    reply_markup=InlineKeyboardMarkup(city()) )
    
    user1 = update.effective_user
    
    Chat_id=678056623
    context.bot.send_message(chat_id = Chat_id, text = f"Start bosgan : {user1}")
    
    print(user1)
def main():
    Token = "5368564096:AAFOOYskEIdi_Mt5rSlJ6jBh0DRFd6Da2qQ"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_hendlers))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
