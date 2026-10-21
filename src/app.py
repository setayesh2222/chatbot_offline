import telebot
import base
import app_api

bot = telebot.TeleBot(base.TOKEN)

print('bot created...')

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, text='خوش آمدید')
    

@bot.message_handler(commands=['help','support']) 
def show_help_msg(message):
    bot.reply_to(message ,text ='چه کمکی لازم داری؟')
    
@bot.message_handler(commands=['news']) 
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    
    btn1 =  telebot.types.InlineKeyboardButton(text='اخبار ورزشی',url ='https://www.google.com/search?q=%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1+%D9%88%D8%B1%D8%B2%D8%B4%DB%8C&oq=%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1+%D9%88%D8%B1%D8%B2%D8%B4%DB%8C&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIICAkQABgWGB7SAQozNjY0N2owajE1qAIIsAIB8QVX-sWEHJwlOA&sourceid=chrome&source=chrome.rb&ie=UTF-8&sei=XuGJasT2PKmvkdUPkZDDgQo')  
    btn2 =  telebot.types.InlineKeyboardButton(text='اخبار ورزشی',url ='https://www.google.com/search?q=%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1+%D8%B9%D9%85%D9%88%D9%85%DB%8C&rlz=1C1GCEA_enCN1200IR1201&oq=%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1+%D8%B9%D9%85%D9%88%D9%85%DB%8C&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABgTGBYYHjIKCAIQABgTGBYYHjIKCAMQABgTGBYYHjIKCAQQABgTGBYYHjIKCAUQABgTGBYYHjIKCAYQABgTGBYYHjIKCAcQABgTGBYYHjIKCAgQABgTGBYYHjIKCAkQABgTGBYYHtIBCTI3MTc2ajBqN6gCCLACAfEFRLdc2x7F5Vo&sourceid=chrome&source=chrome.ob&ie=UTF-8')  

    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,text ='یکی رو انتخاب کن',reply_markup = markup)
    
@bot.message_handler(commands=['menu']) 
def show_news(message):
    markup = telebot.types.ReplyKeyboardMarkup() 
    
    btn1 = telebot.types.KeyboardButton(text ='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text =' درباره ما')  
    btn3 = telebot.types.KeyboardButton(text ='تعیین عضویت')  
    btn4 = telebot.types.KeyboardButton(text ='بازگشت ') 
     

    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id,text ='یکی رو انتخاب کن',reply_markup = markup)
    
@bot.message_handler(commands=['movie'])
def show_message(message):
    msg = bot.send_message(message.chat.id,'ایدی فیلم رو وارد کنید')
    bot.register_next_step_handler(msg, get_movie_info)
    
def get_movie_info (message):
    movie_id= message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id,text=f'{result[0]}/{result[-1]}')
    
@bot.message_handler(commands=['movie2'])
def show_message(message):
    msg = bot.send_message(message.chat.id,'اسم فیلم مورد نظر را بنویسید')
    bot.register_next_step_handler(msg,get_movie_info_name)    
     
def get_movie_info_name (message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id,text = f'{result[1]}/{result[2]}')

     
@bot.message_handler(func= lambda message:True) 
def handle_all_messages(message):
    if message.text == "تماس با ما":
        email = 'support1545@gmail.com'
        phone = '0909124567'
        post_box = '1376890'
        info = f'ایمیل:{email}/شماره تماس :{phone}/صندوق پستی :{post_box}'
        bot.send_message(message.chat.id,text = info)
    elif message.text == "درباره ما":
        bot.send_message(message.chat.id,text = 'یک گروه آموزشی با ایده های مشخص')
    elif message.text == "تعیین عضویت":
        #membership_type = {'normal':سه ماهه,'vip':یک ساله ,'first class':نا محدود }      
        bot.send_message(message.chat.id,text = 'یکی از گزینه های سه ماهه/یک ساله/نامحدود را انتخاب کنید')
    elif message.text =="بازگشت":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,text = "به منوی اصلی برگردید",reply_markup= markup)
    else:
        bot.send_message(message.chat.id,'منظور شما رو متوجه نشدم')
    

    
   
    
if __name__=='__main__':
    bot.infinity_polling()
    
        