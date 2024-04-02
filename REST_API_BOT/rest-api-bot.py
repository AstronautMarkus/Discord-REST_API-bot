import discord
import requests
import random
import asyncio


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

# Kanye Rest API https://kanye.rest/
    
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
        await interaction.response.send_message(f"https://http.cat/{response.status_code}")

# WAIFU.PICS API https://waifu.pics/

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
        await interaction.followup.send(f"https://http.cat/{response.status_code}")

# Cat Facts API https://catfact.ninja/


@bot.tree.command(name="cat_fact", description="Get a random fact about cats! 🐱")
async def catFacts(interaction: discord.Interaction):
    url = "https://catfact.ninja/fact"

    response = requests.get(url) # GET petition

    # REST logic

    if response.status_code == 200:

        data = response.json()

        fact = data['fact']

        await interaction.response.send_message(f"a fact about cats: {fact} 🐈")
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")
        await interaction.followup.send(f"https://http.cat/{response.status_code}")

# Bored https://www.boredapi.com/

@bot.tree.command(name="bored", description="Are you bored? look this!")
async def boredCommand(interaction: discord.Interaction):

    url = "https://www.boredapi.com/api/activity"

    response = requests.get(url) # GET petition

    # REST logic

    if response.status_code == 200:

        data = response.json()

        activity = data['activity']
        type = data['type']
        participants = data['participants']

        embed = discord.Embed(
        title="An activity for you",
        description=activity,
        color=discord.Color.blue()
        )
        embed.add_field(name="Type", value=type, inline=False)
        embed.add_field(name="Participants", value=participants, inline=False)


        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")
        await interaction.followup.send(f"https://http.cat/{response.status_code}")


# WAIFU.PICS (NSFW with protection) https://waifu.pics/
        
@bot.tree.command(name="waifu_img_nsfw", description="Use at your own risk!")
async def waifuImgNSFW(interaction: discord.Interaction):

    # Check if the channel is NSFW
    if interaction.channel.is_nsfw():
        nsfw_allowed = True
    else:
        await interaction.response.send_message(f"Sorry, this channel `{interaction.channel.name}` doesn't allow NSFW content.")
        return

    url = "https://api.waifu.pics/sfw/waifu" if not nsfw_allowed else "https://api.waifu.pics/nsfw/waifu"  # API url

    response = requests.get(url)  # GET request

    # REST logic
    if response.status_code == 200:
        data = response.json()
        img_waifu = data['url']

        if nsfw_allowed:
            await interaction.response.send_message(f"||{img_waifu}||")
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")
        await interaction.followup.send(f"https://http.cat/{response.status_code}")


@bot.tree.command(name="joke", description="Use if you want a random joke.")
async def jokeCommand(interaction: discord.Interaction):

    url = "https://official-joke-api.appspot.com/jokes/random"

    response = requests.get(url) # GET petition

    # REST logic

    if response.status_code == 200:

        data = response.json()

        setup = data['setup']
        type = data['type']
        punchline = data['punchline']

        embed = discord.Embed(
        title="A random joke",
        description=setup,
        color=discord.Color.red()
        )
        embed.add_field(name="", value=punchline, inline=False)
        embed.add_field(name="Type", value=type, inline=False)


        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"Sorry, the request could not be made at this time. Reason: {response.status_code}")
        await interaction.followup.send(f"https://http.cat/{response.status_code}")


# commands list ends here



bot.run("TOKEN_HERE") #ALWAYS change before commits :)




''' Example tree.command


@bot.tree.command(name="name", description="description")
async def nameDef(interaction: discord.Interaction):

    # command here!


'''


'''

Embed example!

@bot.tree.command(name="name", description="description")
async def nameDef(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Título del Embed",
        description="Descripción del Embed",
        color=discord.Color.blue()  # Puedes cambiar el color según tus preferencias
    )
    embed.add_field(name="Campo 1", value="Valor 1", inline=False)
    embed.add_field(name="Campo 2", value="Valor 2", inline=False)
    # Añade más campos si lo necesitas

    await interaction.response.send_message(embed=embed)


'''