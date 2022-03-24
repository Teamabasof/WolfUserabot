def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./herlockuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(herlock):
	for i in a:
		await herlock.edit(' '+str(i))
		sleep({slep})
Help = CmdHelp("herlockuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @HerlockUserBot1 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def a_(fayl_adi, name, siyahi, slep):
	f = open(f"./herlockuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(herlock):
	text= " "
	for i in a:
		text+=i+"\\n"
		await herlock.edit(text)
		sleep({slep})
Help = CmdHelp("herlockuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @HerlockUserBot1 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def r_(fayl_adi, name, siyahi):
	f = open(f"./herlockuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from random import choice
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(herlock):
	random_ = choice(a)
	await herlock.client.send_file(herlock.chat_id, random_)
	await herlock.delete()
Help = CmdHelp("herlockuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @HerlockUserBot1 tarafından hazırlanmıştır.")
Help.add()
		""")

def m_(fayl_adi, name, siyahi):
	f = open(f"./herlockuserbot{fayl_adi}.py", "x")
	f.write("""from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import random
import os
IFACI = [{siyahi}]
@register(outgoing=True, pattern="^.{name}$")
async def herlockmusic(herlock):
    
    
    await herlock.edit("`Sizin için  "+IFACI+"müziğini aktarıyorum`")
    try:
        results = await herlock.client.inline_query('deezermusicbot', '+IFACI+')
    except:
            await herlock.edit("`Bottan cevap alamadım`")
            return
    netice = False
    while netice is False:
            rast = random.choice(results)
            if rast.description == IFACI:
                await herlock.edit("`Müzik Yükleniyor!")
                yukle = await rast.download_media()
                await herlock.edit("`Yükleme tamamlandı!`")
                await herlock.client.send_file(herlock.chat_id, yukle, caption="@HerlockUserBot1 sizin için `"+rast.description+" - "+rast.title+"` müziğini seçti iyi dinlemeler. :)")
                await event.delete()
                os.remove(yukle)
                netice = True
Help = CmdHelp("herlockuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @HerlockUserBot1 Taradındən Hazırlanmışdır..")
Help.add()
		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))
