
from telethon import events 
import time 
import asyncio 
from userbot.events import register

@register(outgoing=True,pattern="^.[Ss]iri")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Siri Yazmak Yerine__ `.herlock` __Yazmalısın.__\n \n**Gerekli Açıklama:** t.me/HerlockUserBot/65 \n UserBot Kanalı: @HerlockUserBot\nPlugin Kanalı: @HerlockPlugin")

@register(outgoing=True,pattern="^.[Oo]wen")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Epic Yazmak Yerine__ `.herlock` __Yazmalısın.__\n \n**Gerekli Açıklama:** https://t.me/HerlockUserBot/80 \n UserBot Kanalı: @HerlockUserBot\nPlugin Kanalı: @HerlockPlugin")
