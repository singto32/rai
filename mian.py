from os import getenv

import os
import discord
from discord.ext import commands

from myserver import server_on

# ตั้งค่า intents
intents = discord.Intents.default()
intents.message_content = True  # สำคัญ!

# ใส่ ID ของช่องที่ต้องการให้บอทตอบ

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = "MTMzNjAwNzA1NzgwMjc5MzAwMg.GNISjw.mSIeblY6BrFIo6WjlG5KWYA7kTtV5zjy_OpX9A"

@bot.event
async def on_ready():
    print(f"✅ Bot is online! Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # เช็คว่าข้อความมาจากช่องที่กำหนดหรือไม่
    if message.channel.id != TARGET_CHANNEL_ID:
        return  # ถ้าไม่ใช่ช่องที่กำหนด บอทจะไม่ตอบ

    print(f"📩 ได้รับข้อความ: {message.content}")  # Debug

    if "hello" in message.content.lower():
        await message.channel.send("Hello am gay")

    if "kuy" in message.content.lower():  # ใช้ `in` เพื่อตรวจว่ามี kuy อยู่ในข้อความ
        await message.channel.send("podee")

    await bot.process_commands(message)  # สำคัญ!

server_on()

bot.run(os.getenv('TOKEN'))
