import discord
import requests
import random

from discord.ext import commands


bot = commands.Bot(command_prefix="_", intents=discord.Intents.all())


@bot.event  #only for check bot status on startup
async def on_ready():
    print(f"Started bot as: {bot.user}")

@bot.command() #synchronize commands for the bot
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("Ready!")

# commands list starts here

@bot.tree.command(name="ping", description="Check the latency of your connection to the Discord server")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency_ms}ms")

# Kanye Rest API command
    
@bot.tree.command(name="kanyequote", description="Get a random quote of Kanye West.")
async def kanyeQuote(interaction: discord.Interaction):

    url = "https://api.kanye.rest/" # API url

    response = requests.get(url) # GET petition

    # REST logic

    if response.status_code == 200:

        data = response.json()

        quote = data['quote']

        await interaction.response.send_message(quote)
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")

@bot.tree.command(name="waifu_img", description="Get a random SFW image of anime girl.")
async def waifuImg(interaction: discord.Interaction):

    url = "https://api.waifu.pics/sfw/waifu" # API url

    response = requests.get(url) # GET petition

    # REST logic

    if response.status_code == 200:

        data = response.json()

        img_waifu = data['url']

        await interaction.response.send_message(img_waifu)
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")


# commands list ends here


bot.run("TOKEN_HERE") #ALWAYS change before commits :)