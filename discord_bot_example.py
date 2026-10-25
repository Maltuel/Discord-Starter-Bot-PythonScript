
# imports --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from discord.ext import commands
import discord

# variables and tokens --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BOT_TOKEN = "X"
SERVER_ID = 1

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# bot starting event --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print('---------------------------------------------')
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('---------------------------------------------')

# bot mentioned event --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user in message.mentions:
        await message.channel.send("I was mentioned!")
        print('Bot mentioned at ' + str(message.created_at) + ' by ' + str(message.author) + ' in ' + str(message.channel))
    await bot.process_commands(message)

# bot functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def commands(ctx):
    await ctx.send("Available commands are: \n !commands \n !ping")
    print('Helper command used at ' + str(ctx.message.created_at) + ' by ' + str(ctx.message.author) + ' in ' + str(ctx.message.channel))

@bot.command()
async def ping(ctx):
    await ctx.send(f'_Pong!_\n**Latenz:** {round(bot.latency * 1000)} ms')
    print('Ping command used at ' + str(ctx.message.created_at) + ' by ' + str(ctx.message.author) + ' in ' + str(ctx.message.channel))

# bot run --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot.run(BOT_TOKEN)