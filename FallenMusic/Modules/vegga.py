import asyncio

import os
import time
import requests
from config import START_IMG
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from FallenMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين القرش","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cde2b51203fbdab57fac5.jpg",
        caption=f"""**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين القرش ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★᚜⎖᳒𝐎𝐌𝐀𝐑𐇲⌯‹♱᚛★", url=f"https://t.me/T_3_A"), 
                 ],[
                    InlineKeyboardButton(
                        "★᚜𝐻𝐴𝑆𝑆𝐴𝑁᚛★", url=f"https://t.me/QF_QG"),
                ],[
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⚡", url=f"https://t.me/L_H_V"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["حسن"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("QF_QG")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
    
   



