import discord
from discord.ext import commands
import random

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command 1: Ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Command 2: Hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Command 3: Random Number
@bot.command(name='random')
async def random_number(ctx):
    number = random.randint(1, 100)
    await ctx.send(f'Your random number is {number}')

# Command 4: Embed Example
@bot.command(name='embed')
async def embed_example(ctx):
    embed = discord.Embed(title="Embed Title", description="This is an embedded message", color=0x00ff00)
    embed.add_field(name="Field1", value="This is a field", inline=False)
    embed.set_footer(text="Footer text")
    await ctx.send(embed=embed)

# Command 5: User Info
@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title="User Info", color=0x00ff00)
    embed.add_field(name="Name", value=member.name)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Joined At", value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'))
    await ctx.send(embed=embed)

# Command 6: Server Info
@bot.command(name='serverinfo')
async def serverinfo(ctx):
    embed = discord.Embed(title="Server Info", color=0x00ff00)
    embed.add_field(name="Server Name", value=ctx.guild.name)
    embed.add_field(name="Total Members", value=ctx.guild.member_count)
    embed.add_field(name="Server Region", value=ctx.guild.region)
    await ctx.send(embed=embed)

# Command 7: Choose
@bot.command(name='choose')
async def choose(ctx, *choices):
    choice = random.choice(choices)
    await ctx.send(f'I choose: {choice}')

# Command 8: Joke
@bot.command(name='joke')
async def joke(ctx):
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!"
    ]
    await ctx.send(random.choice(jokes))

# Command 9: Roll Dice
@bot.command(name='roll')
async def roll(ctx, sides: int):
    result = random.randint(1, sides)
    await ctx.send(f'You rolled a {result} on a {sides}-sided die!')

# Command 10: Weather (Placeholder)
@bot.command(name='weather')
async def weather(ctx, *, location):
    await ctx.send(f'The weather in {location} is currently sunny with a chance of rain.')

# Command 11: Emoji Reaction
@bot.command(name='react')
async def react(ctx):
    emojis = ['😀', '😂', '😍', '😎', '😢']
    await ctx.send(f'Here is a random emoji: {random.choice(emojis)}')

# Command 12: Clear Messages
@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages!', delete_after=5)

# Command 13: Kick User
@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for reason: {reason}')

# Command 14: Ban User
@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for reason: {reason}')

# Command 15: Unban User
@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user.mention}')

# Command 16: Avatar
@bot.command(name='avatar')
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

# Command 17: Server Icon
@bot.command(name='servericon')
async def servericon(ctx):
    await ctx.send(ctx.guild.icon.url)

# Command 18: Add Role
@bot.command(name='addrole')
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'Added role {role.name} to {member.mention}')

# Command 19: Remove Role
@bot.command(name='removerole')
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'Removed role {role.name} from {member.mention}')

# Command 20: Bot Info
@bot.command(name='botinfo')
async def botinfo(ctx):
    embed = discord.Embed(title="Bot Info", color=0x00ff00)
    embed.add_field(name="Bot Name", value=bot.user.name)
    embed.add_field(name="Bot ID", value=bot.user.id)
    embed.add_field(name="Servers", value=len(bot.guilds))
    await ctx.send(embed=embed)

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
