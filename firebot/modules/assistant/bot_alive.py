from firebot import ALIVE_NAME
from firebot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/de27740783234c27fa834.jpg"
pm_caption = "➥ **HEYA NELLY IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.23.0` \n"
pm_caption += "➥ **Python:** `3.9.0` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n\n"
pm_caption += "➥ **SupportGroup** :  [HERE](https://t.me/Kayaspirerproject)\n"
pm_caption += "[Support Channel](https://t.me/xprograming)"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def fire(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
