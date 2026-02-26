from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class PRO(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="Clonify",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
            chat_member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).warning(
                    "Bot can access LOGGER_ID but is not admin there. Some log/channel features may not work."
                )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, errors.ChatAdminRequired):
            LOGGER(__name__).warning(
                "Bot has failed to access the log group/channel. Please add the bot to LOGGER_ID and promote it as admin. Continuing startup without logger checks."
            )
        except ValueError:
            LOGGER(__name__).warning(
                "LOGGER_ID appears to be invalid. Use a valid Telegram chat ID (e.g. -100xxxxxxxxxx). Continuing startup without logger checks."
            )
        except Exception as ex:            
            LOGGER(__name__).warning(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}. Continuing startup without logger checks."
            )

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
        
