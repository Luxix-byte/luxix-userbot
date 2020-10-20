"""Check if userbot ionix. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: ShaDow Gang
import time
from uniborg.util import admin_cmd, sudo_cmd
from userbot import LUXIX_NAME
from datetime import datetime
from userbot import Lastupdate
from userbot.plugins import currentversion

#Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(LUXIX_NAME) if LUXIX_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/8a56360a3bf7e64f9d8d0.jpg"'
"https://telegra.ph/file/f1891bdd10dca16400214.jpg"'
"https://telegra.ph/file/2da5eeb4a8be3f12b8f8e.jpg"'
"https://telegra.ph/file/1a4577d83256da44d5f9d.jpg"'
"https://telegra.ph/file/a4d7263daf517cfd20014.jpg"']
pm_caption = "🟢 **MADE IN 🇳🇪 MADE FOR LUXIX**\n\n"
pm_caption += "🔵 **SYSTEMS STATS**\n"
pm_caption += "🟢 `Telethon Version:` **1.15.0** \n"
pm_caption += "🔵 `Python:` **3.7.4** \n"
pm_caption += f"🟢 `Uptime` : **{uptime}** \n"
pm_caption += "🔵 `Database Status:`  **Functional**\n"
pm_caption += "🟢 `Join` [Support Channel](t.me/RkProjects)/n"
pm_caption += "[Deploy✔️](https;//github.com/luxix-byte/Luxix-userbot)"


@borg.on(admin_cmd(pattern=r"luxix"))
@borg.on(sudo_cmd(pattern=r"luxix", allow_sudo=True))
async def luxix(luxix):
    await luxix.get_chat()
    """ For .luxix command, check if the bot is running.  """
    await borg.send_file(luxix.chat_id, PM_IMG, caption=pm_caption)
    await luxix.delete()
