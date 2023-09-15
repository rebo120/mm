import os
import requests
import telebot, threading
from telebot import types
from timeit import default_timer as timer

admin = 6158116713 #owner id

chat_id = "PyThOnX1" #ur channel user

dev = "M_M_F_F" #ur username

token = "6401572204:AAEF61iyvDCek9pyKKRBHTAOXmQtLD9Ut2c"

bot = telebot.TeleBot(token, num_threads=50, skip_pending=True, parse_mode="markdown", disable_web_page_preview=True)

@bot.message_handler(commands=["start"])
def welcome(message):
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{chat_id}&user_id={message.from_user.id}")
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        try:
        	Tho = open("id.txt").read()
        except:
        	oo = open("id.txt", "a")
        	Tho = open("id.txt").read()
        try:
        	ban = open("ban.txt").read()
        except:
        	bb = open("ban.txt", "a")
        	ban = open("ban.txt").read()
        try:
        	ad = open("ad.txt").read()
        except:
        	yy = open("ad.txt", "a")
        	ad = open("ad.txt").read()
        if str(message.from_user.id) == str(admin):
    	    keyboard = types.InlineKeyboardMarkup()
    	    keyboard.row_width = 1
    	    Tho1 = types.InlineKeyboardButton("اذاعة",callback_data="brod")
    	    Tho2 = types.InlineKeyboardButton("أرسل التخزين",callback_data="file")
    	    Tho3 = types.InlineKeyboardButton(f"الأحصائيات",callback_data="info")
    	    Tho4 = types.InlineKeyboardButton(f"حظر مستخدم",callback_data="ban")
    	    Tho5 = types.InlineKeyboardButton(f"مسح المحظورين",callback_data="allun")
    	    Tho6 = types.InlineKeyboardButton(f"الغاء حظر",callback_data="unban")
    	    Tho7 = types.InlineKeyboardButton(f"رفع أدمن",callback_data="adad")
    	    Tho8 = types.InlineKeyboardButton(f"تنزيل أدمن",callback_data="unad")
    	    Tho9 = types.InlineKeyboardButton(f"مسح جميع الادمنية",callback_data="rmad")
    	    keyboard.row(Tho3, Tho2)
    	    keyboard.row(Tho1)
    	    keyboard.row(Tho6, Tho4)
    	    keyboard.row(Tho5)
    	    keyboard.row(Tho8, Tho7)
    	    keyboard.row(Tho9)
    	    bot.reply_to(message, f"*أهلا بك عزيزي المالك*", reply_markup=keyboard)
    	    btn = types.InlineKeyboardMarkup()
    	    btn.row_width = 1
    	    ah = types.InlineKeyboardButton("المطور", url=f"t.me/{dev}")
    	    mho = types.InlineKeyboardButton(f"سحب معلومات الـ IP",callback_data="IP")
    	    btn.add(mho,ah)
    	    bot.reply_to(message, "أهلا بك عزيزي المستخدم", reply_markup=btn)
    	    
        elif str(message.from_user.id) in ban:
        	bot.reply_to(message, "*تم حظرك من البوت\nللأستفسار عن السبب راسل المطور*")
        elif str(message.from_user.id) in ad:
    	    keyboard = types.InlineKeyboardMarkup()
    	    keyboard.row_width = 1
    	    Tho1 = types.InlineKeyboardButton("اذاعة",callback_data="brod")
    	    Tho3 = types.InlineKeyboardButton(f"الأحصائيات",callback_data="info")
    	    Tho4 = types.InlineKeyboardButton(f"حظر مستخدم",callback_data="ban")
    	    Tho6 = types.InlineKeyboardButton(f"الغاء حظر",callback_data="unban")
    	    keyboard.row(Tho1, Tho3)
    	    keyboard.row(Tho4, Tho6)
    	    bot.reply_to(message, f"*أهلا بك عزيزي الادمن*", reply_markup=keyboard)
    	    bot.reply_to(message, "أهلا بك عزيزي المستخدم")
    	    
        elif str(message.from_user.id) in Tho:
            btn = types.InlineKeyboardMarkup()
            btn.row_width = 1
            ah = types.InlineKeyboardButton(text="المطور", url=f"t.me/{dev}")
            mho = types.InlineKeyboardButton(f"سحب معلومات الـ IP",callback_data="IP")
            btn.add(mho,ah)
            bot.reply_to(message, "أهلا بك عزيزي المستخدم", reply_markup=btn)
        else:
    	    with open("id.txt", "a") as Ah:
    	    	Ah.write(f"{message.from_user.id}\n")
    	    bot.reply_to(message, "*تم تفعيل البوت\nأرسل /start*")
    	    bot.send_message(admin, f"*مستخدم جديد:\nإسمه:* {message.from_user.first_name} .\n*يوزرة:* @{message.from_user.username} .\n*أيديه:* `{message.from_user.id}` .\n[المبرمج](t.me/{dev})")
    else:
    	bot.reply_to(message, f"*لازم تشترك بقناة البوت حتى تكدر تستخدمة\n\n- @{chat_id}*")

@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "file":
    	bot.send_document(admin, open('id.txt','rb'))
    	try:
    		bot.send_document(admin, open('ban.txt','rb'))
    	except:
    		bot.send_message(admin, "*لايوجد محظورين لأرسال ملفهم*")
    if call.data == "brod":
    	bot.send_message(call.message.chat.id, "*أرسل رسالة الاذاعة\nتگدر تستعمل ماركداون همين*")
    	bot.register_next_step_handler(call.message, brod)
    if call.data=='IP':
        bot.send_message(call.message.chat.id,'ارسل الان الـ ip')
@bot.message_handler(func=lambda m: True)
def info(message):
    msg = message.text
    try:
    	url = requests.get(f'https://ipinfo.io/{msg}/geo').json()
    	ip = url['ip']
    	ci = url['city']
    	reg = url['region']
    	co = url['country']
    	l = url['loc']
    	org = url['org']
    	tim = url['timezone']
    	bot.send_message(message.chat.id, f'''
    معلومات  ~ {ip} ⤵️


مدينة : {ci}
منطقة : {reg}
رمز الدولة : {co}
المكان : {l}
السكن : {org}
الوحدة الزمنية : {tim}
  ''')
  
    except:
           bot.send_message(message.chat.id,'تأكد من صحة ip ..')     	
    	
    	

    if call.data == "info":
    	Th = open("id.txt", "r")
    	Of = open("ban.txt", "r")
    	adr = open("ad.txt", "r")
    	qa = len(Th.readlines())
    	ar = len(Of.readlines())
    	ad = len(adr.readlines())
    	bot.send_message(call.message.chat.id, f"*أهلا بك عزيزي الادمن في قسم الاحصائيات\nعدد مستخدمين البوت: {qa}.\nعدد المحظورين: {ar}.\nعدد الأدمنية: {ad}.*")
    	Th.close()
    	Of.close()
    	adr.close()
    	
    if call.data == "ban":
    	bot.send_message(call.message.chat.id, "*أرسل الايدي الذي تريد حظره*")
    	bot.register_next_step_handler(call.message, ban)
    	
    if call.data == "allun":
    	try:
    		bot.send_document(admin, open('ban.txt','rb'))
    		os.remove("ban.txt")
    		bot.send_message(admin, "*تم مسح جميع المحظورين و أرسال لك نسخة احتياطية*")
    	except:
    		bot.send_message(call.message.chat.id, "*لا يوجد محظورين*")

    if call.data == "rmad":
    	try:
    		os.remove("ad.txt")
    		bot.send_message(admin, "تمت حبي")
    	except:
    		bot.send_message(call.message.chat.id, "*لا يوجد ادمنيه*")
 
    if call.data == "unban":
    	bot.send_message(call.message.chat.id, "*أرسل الايدي الذي تريد الغاء حظره*")
    	bot.register_next_step_handler(call.message, unban)

    if call.data == "adad":
    	bot.send_message(call.message.chat.id, "*أرسل أيدي المستخدم*")
    	bot.register_next_step_handler(call.message, adad)
    	
    if call.data == "unad":
    	bot.send_message(call.message.chat.id, "*أرسل أيدي المستخدم*")
    	bot.register_next_step_handler(call.message, unad)    	

def unad(message):
	id = message.text
	unad = open("ad.txt").read()
	if id not in unad:
		bot.reply_to(message, "مو أدمن اصلا هذا")
	else:
		name = "ad.txt"
		with open(name, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		lines = [line for line in lines if id not in line]
		with open(name, 'w', encoding='utf-8') as file:
			file.writelines(lines)
		bot.send_message(id, "*تم تنزيلك من الادمنية*")
		bot.reply_to(message, "*تمت حب*")


def adad(message):
    id = message.text
    ad = open("ad.txt").read()
    if id in ad:
    	bot.reply_to(message, "*هذا المستخدم اصلا أدمن*")
    else:
        with open("ad.txt", "a") as Ah:
        	Ah.write(f"{id}\n")
        bot.send_message(id, "*تم رفعك ادمن بالبوت*")
        bot.reply_to(message, "*تمت حبي*")	
		
def unban(message):
	id = message.text
	unbann = open("ban.txt").read()
	if id not in unbann:
		bot.reply_to(message, "مو محظور اصلا حبي")
	else:
		name = "ban.txt"
		with open(name, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		lines = [line for line in lines if id not in line]
		with open(name, 'w', encoding='utf-8') as file:
			file.writelines(lines)
		bot.send_message(id, "*تم الغاء حظرك الان!*")
		bot.reply_to(message, "*تمت حب*")

def ban(message):
    id = message.text
    bann = open("ban.txt").read()
    if id in bann:
    	bot.reply_to(message, "*هذا المستخدم اصلا محظور حبي*")
    else:
        with open("ban.txt", "a") as Ah:
        	Ah.write(f"{id}\n")
        bot.send_message(id, "*تم حظرك من البوت\nللأستفسار راسل المطور*")
        bot.reply_to(message, "*تمت حبي*")

def brod(message):
    msg = message.text
    bot.send_message(admin, msg)    
    ids = open("id.txt", "r").readlines()
    i = 0
    F = 0
    T = 0
    start = timer()
    for Id in ids:
        i = i + 1
        try:
            bot.send_message(Id, msg)
            T = T + 1
        except:
            F = F + 1
    end = timer()
    ttt = end - start
    bot.reply_to(message, f'''*عدد المستخدمين: {len(ids)}
تمت الاذاعة لـ: {T}/{len(ids)}
فشلت لـ: {F}/{len(ids)}
أجمالي وقت الاذاعة : {int(ttt)}*''')
	
print("-- Bot Started...")
bot.infinity_polling()