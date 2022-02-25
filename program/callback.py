# Copyright (C) 2022 By SanthuMusicProjects

from driver.core import me_bot
from driver.decorators import check_blacklist
from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    BG_IMG,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)



@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("home start")
    await query.edit_message_text(
        f"""💝 **ᴡᴇʟᴄᴏᴍᴇ🎉 {message.from_user.mention()} !**\n
🤖 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ🎶 ᴀɴᴅ ᴠɪᴅᴇᴏ🎥 ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ!**

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
                        "💝 sᴀɴᴛʜᴜ ɴᴇᴛᴡᴏʀᴋ 🤎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❤ ʏᴏᴜᴛᴜʙᴇ 💚", url="https://youtube.com/channel/UC7QMr8IDR65vciXrwx4XLiQ"
                    ), 
                    InlineKeyboardButton(
                        "💛 ᴄʜᴀɴɴᴇʟ ☺", url="https://t.me/{GROUP_SUPPORT}"
                    ) 
                ], 
            ]
        ), 
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("help_command"))
@check_blacklist()
async def help(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("help message")
    await query.edit_message_text(
        f""" ✨ **ʜᴇʟʟᴏ [{query.message.chat.first_name}] !**\n
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

# This is not used it will be added in new update
'''@Client.on_callback_query(filters.regex("ghelp_command")) 
@check_blacklist()
async def ghelp(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("help message")
    await query.edit_message_text(
        f""" ✨ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
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
        )'''

@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""📖 ǫᴜɪᴄᴋ ᴜsᴇ ɢᴜɪᴅᴇ ʙᴏᴛ, ᴘʟᴇᴀsᴇ ʀᴇᴀᴅ ғᴜʟʟʏ !

🎻 /play - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ sᴏɴɢ ᴛɪᴛʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ. (ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)

🎺 /vplay - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ sᴏɴɢ ᴛɪᴛʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ. (ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)

🥁 /vstream - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏ ʟɪɴᴋ ᴏʀ ᴍ𝟹ᴜ𝟾 ʟɪɴᴋ ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ. (ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʟᴏᴄᴀʟ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ғɪʟᴇs ᴏʀ ɴᴏɴ-ʟɪᴠᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)

🤨 sᴛɪʟʟ ʜᴀᴠᴇ ǫᴜᴇsᴛɪᴏɴs? ᴄᴏɴᴛᴀᴄᴛ ᴜs ɪɴ [sᴀɴᴛʜᴜ ᴠᴄ](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("◁ ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴇʟᴘ", callback_data="help_command")],
                [InlineKeyboardButton("◁ ʀᴇᴛᴜʀɴ ᴛᴏ sᴇᴛ ᴜᴘ", callback_data="user_guide")]    
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    ass_uname = me_bot.first_name
    await query.answer("user guide")
    await query.edit_message_text(
        f"""🤔 ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ ?, ʀᴇᴀᴅ ᴛʜᴇ ɢᴜɪᴅᴇ ʙᴇʟᴏᴡ !

𝟷.) ғɪʀsᴛ, ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸.) ᴛʜᴇɴ, ᴘʀᴏᴍᴏᴛᴇ ᴛʜɪs ʙᴏᴛ ᴀs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ᴏɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀʟsᴏ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪssɪᴏɴs ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ.
𝟹.) ᴀғᴛᴇʀ ᴘʀᴏᴍᴏᴛɪɴɢ ᴛʜɪs ʙᴏᴛ, ᴛʏᴘᴇ /ʀᴇʟᴏᴀᴅ ɪɴ ɢʀᴏᴜᴘ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ.
𝟹.) ɪɴᴠɪᴛᴇ @{ass_uname} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /ᴜsᴇʀʙᴏᴛᴊᴏɪɴ ᴛᴏ ɪɴᴠɪᴛᴇ ʜᴇʀ, ᴜɴғᴏʀᴛᴜɴᴀᴛᴇʟʏ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴡɪʟʟ ᴊᴏɪɴᴇᴅ ʙʏ ɪᴛsᴇʟғ ᴡʜᴇɴ ʏᴏᴜ ᴜsᴇ sᴏɴɢ ᴘʟᴀʏɪɴɢ ᴄᴏᴍᴍᴀɴᴅs.
𝟺.) ᴛᴜʀɴ ᴏɴ/sᴛᴀʀᴛ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ғɪʀsᴛ ʙᴇғᴏʀᴇ sᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ/ᴍᴜsɪᴄ.

ʀᴇᴀᴅ 
`- ᴇɴᴅ, ᴇᴠᴇʀʏᴛʜɪɴɢ ʜᴀs ʙᴇᴇɴ sᴇᴛᴜᴘ -`

🪀 ɪғ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ, ᴍᴀᴋᴇ sᴜʀᴇ ɪғ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ᴀɴᴅ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

🤸‍♀️ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ғᴏʟʟᴏᴡ-ᴜᴘ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴛᴇʟʟ ɪᴛ ᴏɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʜᴇʀᴇ: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤿ᴜsᴇ ᴛʜɪs ɢᴜɪᴅᴇ🥱", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("◁ ʙᴀᴄᴋ ᴛᴏ ʜᴇʟᴘ", callback_data="home_command")
                ],[
                    InlineKeyboardButton("🏠ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ🏠", callback_data="help_start")
                ]
            ]   
      ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

🏹 ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ & sᴇᴇ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs !

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ (`! / .`) ʜᴀɴᴅʟᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥺ᴀᴅᴍɪɴ ᴄᴍᴅs💔", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("💔ᴜsᴇʀ ᴄᴍᴅs🙄", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("🔰sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs🔰", callback_data="sudo_command"),
                    InlineKeyboardButton("✅ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs💘", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("◁ ʙᴀᴄᴋ ᴛᴏ ʜᴇʟᴘ", callback_data="home_command")
                ],[
                    InlineKeyboardButton("🏠ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ🏠", callback_data="help_start")
                ]
                   
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""💗 ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ғᴏʀ ᴀʟʟ ᴜsᴇʀ.

» /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /vplay (ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /vstream (ᴍ𝟹ᴜ𝟾/ʏᴛ ʟɪᴠᴇ ʟɪɴᴋ) - ᴘʟᴀʏ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏ
» /playlist - sᴇᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ
» /lyric (ǫᴜᴇʀʏ) - sᴄʀᴀᴘ ᴛʜᴇ sᴏɴɢ ʟʏʀɪᴄ
» /video (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ
» /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs
» /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs
» /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)
» /help - ᴛᴏ sʜᴏᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ (ғᴜʟʟ ʙᴏᴛ ɢᴜɪᴅᴇ)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""💘 ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ғᴏʀ sᴀɴᴛʜᴜ ʙᴏᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ.

» /pause - ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ ʙᴇɪɴɢ ᴘʟᴀʏᴇᴅ
» /resume - ᴘʟᴀʏ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜsʟʏ ᴘᴀᴜsᴇᴅ ᴛʀᴀᴄᴋ
» /skip - ɢᴏᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ
» /stop - sᴛᴏᴘ ᴘʟᴀʏʙᴀᴄᴋ ᴏғ ᴛʜᴇ ᴛʀᴀᴄᴋ ᴀɴᴅ ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ
» /vmute - ᴍᴜᴛᴇ ᴛʜᴇ sᴛʀᴇᴀᴍᴇʀ ᴜsᴇʀʙᴏᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴛʜᴇ sᴛʀᴇᴀᴍᴇʀ ᴜsᴇʀʙᴏᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ
» /volume `𝟷-𝟸𝟶𝟶` - ᴀᴅᴊᴜsᴛ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ᴏғ ᴍᴜsɪᴄ (ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ)
» /reload - ʀᴇʟᴏᴀᴅ ʙᴏᴛ ᴀɴᴅ ʀᴇғʀᴇsʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ
» /userbotleave - ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴄʟɪᴄᴋ ᴛʜɪs ʙᴜᴛᴛᴏɴ\n\n» ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ʀᴇsᴇʀᴠᴇᴅ ғᴏʀ sᴜᴅᴏ ᴍᴇᴍʙᴇʀs ᴏғ ᴛʜɪs ʙᴏᴛ.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""💖 ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ғᴏʀ sᴀɴᴛʜᴜ ʙᴏᴛ sᴜᴅᴏ ᴜsᴇʀ.

» /stats - ɢᴇᴛ ᴛʜᴇ ʙᴏᴛ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛɪsᴛɪᴄ
» /calls - sʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀʟʟ ᴀᴄᴛɪᴠᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ
» /block (`ᴄʜᴀᴛ_ɪᴅ`) - ᴜsᴇ ᴛʜɪs ᴛᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ɢʀᴏᴜᴘ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
» /unblock (`ᴄʜᴀᴛ_ɪᴅ`) - ᴜsᴇ ᴛʜɪs ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ ᴀɴʏ ɢʀᴏᴜᴘ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
» /blocklist - sʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀʟʟ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ
» /speedtest - ʀᴜɴ ᴛʜᴇ ʙᴏᴛ sᴇʀᴠᴇʀ sᴘᴇᴇᴅᴛᴇsᴛ
» /sysinfo - sʜᴏᴡ ᴛʜᴇ sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
» /eval - ᴇxᴇᴄᴜᴛᴇ ᴀɴʏ ᴄᴏᴅᴇ (`ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴛᴜғғ`)
» /sh - ʀᴜɴ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ (`ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴛᴜғғ`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("⚠️ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴄʟɪᴄᴋ ᴛʜɪs ʙᴜᴛᴛᴏɴ\n\n» ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ʀᴇsᴇʀᴠᴇᴅ ғᴏʀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""💝 ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ғᴏʀ ʙᴏᴛ sᴀɴᴛʜᴜ ʙᴏᴛ.

» /gban (`ᴜsᴇʀɴᴀᴍᴇ` ᴏʀ `ᴜsᴇʀ_ɪᴅ`) - ғᴏʀ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ ᴘᴇᴏᴘʟᴇ, ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ
» /ungban (`ᴜsᴇʀɴᴀᴍᴇ` ᴏʀ `ᴜsᴇʀ_ɪᴅ`) - ғᴏʀ ᴜɴ-ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ ᴘᴇᴏᴘʟᴇ, ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ
» /restart - ʀᴇsᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ ᴅɪʀᴇᴄᴛʟʏ
» /leaveall - ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ
» /leavebot (`ᴄʜᴀᴛ ɪᴅ`) - ᴏʀᴅᴇʀ ʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ ʏᴏᴜ sᴘᴇᴄɪғʏ
» /broadcast (`ᴍᴇssᴀɢᴇ`) - sᴇɴᴅ ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs ɪɴ ʙᴏᴛ ᴅᴀᴛᴀʙᴀsᴇ
» /broadcast_pin (`ᴍᴇssᴀɢᴇ`) - sᴇɴᴅ ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs ɪɴ ʙᴏᴛ ᴅᴀᴛᴀʙᴀsᴇ ᴡɪᴛʜ ᴛʜᴇ ᴄʜᴀᴛ ᴘɪɴ

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
