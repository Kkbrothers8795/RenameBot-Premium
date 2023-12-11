from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 5GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 20GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

        **VIP 3 **
	Daily Upload limit **∞**GB
	Price Rs 90  🇮🇳/🌎 0.97$  per Month
	
	Pay Using Upi I'd ```hxbots@pingpay```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Kirodewal")], 
        			[InlineKeyboardButton("UPI 🌎",url = "https://t.me/Kirodewal"),
        			InlineKeyboardButton("PayTm ",url = "http://m.p-y.tm/requestPayment?recipient=8742089059")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 5GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 20GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

        **VIP 3 **
	Daily Upload limit **∞**GB
	Price Rs 90  🇮🇳/🌎 0.97$  per Month
	
	Pay Using Upi I'd ```hxbots@pingpay```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Kirodewal")], 
        			[InlineKeyboardButton("UPI 🌎",url = "https://t.me/Kirodewal"),
        			InlineKeyboardButton("PayTm ",url = "http://m.p-y.tm/requestPayment?recipient=8742089059")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	
