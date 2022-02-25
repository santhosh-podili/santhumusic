import asyncio

from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    BG_IMG,
    ALIVE_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from driver.decorators import check_blacklist
from program import __version__
from driver.core import bot, me_bot, me_user
from driver.filters import command
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from driver.database.dbusers import add_served_user
from driver.database.dblockchat import blacklisted_chats
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
@check_blacklist()
async def start_(c: Client, message: Message):
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f"""💝 **ᴡᴇʟᴄᴏᴍᴇ🎉 {message.from_user.mention()} !**\n
😁 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ🎶 ᴀɴᴅ ᴠɪᴅᴇᴏ🎥 ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ!**

💚 **ғɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 🛠️ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!**

💝 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ, ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ » 💚 ʀᴇᴀᴅ ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʙᴜᴛᴛᴏɴ **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 ɴᴀɴᴜ ᴀᴅᴅ ᴄʜᴇsᴜ ᴋᴏʀᴀ ɴɪʙʙᴀ 💞",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("💗 ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʀᴀ ɴɪʙʙᴀ 🤍", callback_data="user_guide")],
                [
                    InlineKeyboardButton("✅ ᴀʀʏᴀ ᴄᴏᴍᴍᴀɴᴅs 💘", callback_data="command_list"),
                    InlineKeyboardButton("🔰 ᴅᴏɴᴀᴛᴇ ʀᴀ ɴɪʙʙᴀ 🔰", url=f"https://t.me/{OWNER_USERNAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "💖 ɢʀᴏᴜᴘ ʀᴀ ɴɪʙʙᴀ 💞", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "💝 ᴀʀʏᴀ ɴᴇᴛᴡᴏʀᴋ 🤎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❤ ʏᴏᴜᴛᴜʙᴇ 💚", url="https://youtube.com/channel/UC7QMr8IDR65vciXrwx4XLiQ"
                    ), 
                    InlineKeyboardButton(
                        "💛 ʙᴜɢs ☺", url="https://t.me/{GROUP_SUPPORT}"
                    ) 
                ], 
            ]
        ), 
        disable_web_page_preview=True,
    )

@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
@check_blacklist()
async def help(c: Client, message: Message):
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ ᴠɪᴅᴇᴏ/ᴀᴜᴅɪᴏ/ʟɪᴠᴇ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                                       "😟ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ💘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton( 
                                       "💝sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs💖", callback_data="sudo_command"
                )
            ],
            [
                InlineKeyboardButton(
                                       "💚ᴀᴅᴍɪɴ ᴄᴍᴅs💚", callback_data="admin_commands"
                )
            ],
            [
                InlineKeyboardButton(
                                       "💖sᴀɴᴛʜᴜ ᴄʜᴀɴɴᴇʟ💖", url=f"https://t.me/{UPDATES_CHANNEL}"
                )
            ],
            [
                InlineKeyboardButton("💝ɴᴇᴛᴡᴏʀᴋ💝", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "◁", callback_data="home_start"
                ),
            ]
            
        ]      
  ),
        disable_web_page_preview=True,
    )
        
@Client.on_message(
    command(["ghelp", f"ghelp@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def ghelp(c: Client, message: Message):
    chat_id = message.chat.id
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ ᴠɪᴅᴇᴏ/ᴀᴜᴅɪᴏ/ʟɪᴠᴇ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                                       "😟ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ💘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton( 
                                       "💝sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs💖", callback_data="sudo_command"
                )
            ],
            [
                InlineKeyboardButton(
                                       "💚ᴀᴅᴍɪɴ ᴄᴍᴅs💚", callback_data="admin_commands"
                )
            ],
            [
                InlineKeyboardButton(
                                       "💖sᴀɴᴛʜᴜ ᴄʜᴀɴɴᴇʟ💖", url=f"https://t.me/{UPDATES_CHANNEL}"
                )
            ],
            [
                InlineKeyboardButton("💝ɴᴇᴛᴡᴏʀᴋ💝", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "◁", callback_data="home_start"
                ),
            ]
            
        ]      
  ),
        disable_web_page_preview=True,
    )




@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    BOT_NAME = me_bot.first_name

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💖ɴᴇᴛᴡᴏʀᴋ💖", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "💚ᴄʜᴀɴɴᴇʟ💚", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ʜᴇʟʟᴏ {message.from_user.mention()}, ɪᴀᴍ {BOT_NAME}**\n\n😊 ᴏᴡɴᴇʀ ɴɪʙʙᴀ 😂: [{ALIVE_NAME}](https://t.me/{OWNER_USERNAME})\n😇 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n😚 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n😍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n🥰 ᴘʏᴛɢᴄᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n😘 ᴜᴘᴛɪᴍᴇ: `{uptime}`\n😊 ᴘᴏᴡᴇʀᴇᴅ ʙʏ: '[{GROUP_SUPPORT}](https://t.me/{GROUP_SUPPORT})'\n❤**ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ, ғᴏʀ ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ & ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴠɪᴅᴇᴏ ᴄʜᴀᴛ [ᴘᴏᴡᴇʀᴇᴅ ʙʏ 😊](https://t.me/santhu_music_bot)**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("💝 `ᴘᴏɴɢ!!`\n" f"💖 `{delta_ping * 1000:.3f} ms`")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💖ɴᴇᴛᴡᴏʀᴋ💖", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "💚ᴄʜᴀɴɴᴇʟ💚", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "😊 sᴀɴᴛʜᴜ ʙᴏᴛ sᴛᴀᴛᴜs:\n"
        f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **ᴜsᴇʀ:** `{message.from_user.mention()}`\n"
        f"• **sᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`\n"
        f"• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** `{GROUP_SUPPORT}`"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💖ɴᴇᴛᴡᴏʀᴋ💖", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "💚ᴄʜᴀɴɴᴇʟ💚", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = me_user.username
    bot_id = me_bot.id
    for member in m.new_chat_members:
        if chat_id in await blacklisted_chats():
            await m.reply(
                "❗️ This chat has blacklisted by sudo user and You're not allowed to use me in this chat."
            )
            return await bot.leave_chat(chat_id)
        if member.id == bot_id:
            return await m.reply(
                "❤️ ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ᴛʜᴇ **Group** !\n\n"
                "ᴀᴘᴘᴏɪɴᴛ ᴍᴇ ᴀs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ɪɴ ᴛʜᴇ **Group**, ᴏᴛʜᴇʀᴡɪsᴇ ɪ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴡᴏʀᴋ ᴘʀᴏᴘᴇʀʟʏ, ᴀɴᴅ ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ᴛʏᴘᴇ  `/userbotjoin` ᴛᴏ ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴄʜᴀᴛ.\n\n"
                "ᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʜᴇɴ ᴛʏᴘᴇ `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💚ᴄʜᴀɴɴᴇʟ💚", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("💖ɴᴇᴛᴡᴏʀᴋ💖", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("💝ᴀssɪsᴛᴀɴᴛ🔥", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )


chat_watcher_group = 10

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    if message.from_user:
        user_id = message.from_user.id
        await add_served_user(user_id)
        return
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\n🚫 **Reason:** potential spammer and abuser."
        )
