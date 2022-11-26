__all__ = [
    "hooks",
]

import random
import re

from pyrogram import Client, filters
from pyrogram.types import Message

from .constants import (
    BRA_MEME_PICTURE,
    MIBIB_FLT,
    MIBIB_STICKER,
    TAP_FLT,
    TAP_STICKER,
    UWU_MEME_PICTURE,
)
from .meta.modules import HooksModule
from .utils import sticker

hooks = HooksModule()


@hooks.add("emojis", filters.regex(r"\b((?:дак\b|кря(?:к.?|\b))|блин)", flags=re.I))
async def on_emojis(message: Message) -> str:
    t = ""
    for match in message.matches:
        m = match[1].lower()
        if m == "дак" or m.startswith("кря"):
            t += "🦆"
        elif m == "блин":
            t += "🥞"
    return t


@hooks.add("tap", (filters.regex(r"\b(?:тык|nsr)\b", flags=re.I) | sticker(TAP_FLT)))
async def on_tap(message: Message) -> None:
    await message.reply_sticker(TAP_STICKER)


@hooks.add("mibib", filters.sticker & sticker(MIBIB_FLT))
async def mibib(client: Client, message: Message) -> None:
    # TODO (2022-02-13): Don't send it again for N minutes
    if random.random() <= (1 / 5):
        await client.send_sticker(message.chat.id, MIBIB_STICKER)


@hooks.add("bra", filters.regex(r"\b(?:бра|bra)\b", flags=re.I))
async def on_bra(message: Message) -> None:
    await message.reply_photo(BRA_MEME_PICTURE)


@hooks.add("uwu", filters.regex(r"\b(?:uwu|owo|уву|ово)\b", flags=re.I))
async def on_uwu(message: Message) -> None:
    await message.reply_photo(UWU_MEME_PICTURE)
