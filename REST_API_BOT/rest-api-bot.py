import discord

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


# commands list ends here


bot.run("TOKEN_HERE") #ALWAYS change before commits :)