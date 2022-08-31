#                     *In The Name Of God*

#                    Developer : AmirEdwin
#                    github : 
#                    discord id : AmirEdwin#9999


import asyncio
import time
from turtle import color
from types import MemberDescriptorType
import discord
from discord.ext import commands
from asyncio import *
import random
from discord import colour
from discord import embeds
from discord.ext import tasks
from discord.ext.commands.errors import DisabledCommand
import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
import random
from discord import embeds
import os
from discord.ext.commands.errors import DisabledCommand
from discord.ext import tasks
import random
from discord import colour
from discord import embeds
import asyncio
import time
from turtle import color, title
from types import MemberDescriptorType
import discord
from discord.ext import commands
from asyncio import *
from turtle import color, title
import discord
import asyncio
from discord.ext import commands
import discord_components
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
from aiohttp import request

import discord
from discord.ext import commands


darsad = random.randint(0, 100)

#-----------------------------------Import ind from------------------------------------------
colors =  [0x0051FF, 0x0042D1, 0xFA73FF, 0x1300D1, 0x00A2D1, 0xFF0000]
#-----------------------------------Colors------------------------------------------

class CONFIG:
    TOKEN = "youre token ;)"
    PREFIX = "@"
    OWNERID = "820703923014598656"
#-----------------------------------Config------------------------------------------

client = commands.Bot(command_prefix=CONFIG.PREFIX)
client.remove_command("help")
#-----------------------------------Remove Command Help------------------------------------------
@tasks.loop(seconds=10.0)
async def my_background_task():
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
        activity_string = '{} servers | @help'.format(len(client.guilds))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} Members"),status=discord.Status.online)
@client.event
async def on_ready():
    print('Logged in as: {}'.format(client.user.name))
    print('Bot user: {}'.format(client.user))
    print('----------------------------')
    print('| created : 24/2/2022       |')
    print('| last updated: 18/3/2022   |')
    print('| Developer: AmirEdwin      |')
    print('----------------------------')
#-----------------------------------Run Bot------------------------------------------
@client.command(aliases=["LOCK", "Lock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel=None):
    if channel == None:
        embed = discord.Embed(title="Lotfan channel mored nazar ra Tag konid!", colour=random.choice(colors))
        embed.set_footer(text="mesal : Lock #x", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title="🔒 channel has been Lock", color=0x8b0003)
        await channel.send(embed=embed)

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```MANAGE_CHANNELS``` دارید",
        )
        await ctx.reply(embed=embed)

#--------------------------------------lOCK CHANNEL---------------------------------------
@client.command(aliases=["unLOCK", "unLock", "UNLOCK", "Unlock", "UNlock", "UNLock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel):
    if channel == None:
        embed = discord.Embed(title="Lotfan channel mored nazar ra Tag konid!", colour=random.choice(colors))
        embed.set_footer(text="mesal : Lock #x", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title="🔒 channel has been unLock", color=0x108602)
        await channel.send(embed=embed)

@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```MANAGE_CHANNELS``` دارید",
        )
        await ctx.reply(embed=embed)

#--------------------------------------Unlock kardan---------------------------------------
@client.event
async def on_guild_join(g):
    success = False
    i = 0
    while not success:
        try:
            embed = discord.Embed(title="exampel", color=0x108602, description="**Baraye didan Command ha mitavanid az ( `@help` ) Estefade Konid!**")
            embed.set_footer(text="Server Poshtebani  : https://discord.gg/RRhSs4zKK4") # metavanid link discord khod ra garar dahid
            await g.channels[i].send(embed=embed)
        except (discord.Forbidden, AttributeError):
            i += 1
        except IndexError:
            pass
        else:
            success = True
    payload = {
        'server_count': len(client.guilds)
    }
#--------------------------------------vaghti join server shod payam dahad!---------------------------------------
@client.command(aliases=["user", "User"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.choice(colors), timestamp=ctx.message.created_at,
                          title=f"User Info  {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Darkhast Tavasot: {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="نام <a:user:1005425759680204871>", value=member.display_name)
    embed.add_field(name="ایدی عددی <a:user:1005425759680204871>", value=member.id)

    embed.add_field(name="زمان ساخت اکانت <a:user:1005425759680204871>", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p "))
    embed.add_field(name="زمان جوین سرور <a:user:1005425759680204871>", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p "))

    embed.add_field(name="مقام ها <a:user:1005425759680204871>", value="".join([role.mention for role in roles]))
    embed.add_field(name="بالاترین مقام <a:user:1005425759680204871>", value=member.top_role.mention)

    await ctx.reply(embed=embed)
#--------------------------------------User Info---------------------------------------


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f" shoma unmute shodid! **( {member.name} )**", color=0x036103)
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f" shoma unmute shodid az server: **( {ctx.guild.name} )**", color=0x036103)
    await member.send(embed=embed)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```ADMINISTRATOR``` دارید",
        )
        await ctx.reply(embed=embed)

#--------------------------------------unmute server---------------------------------------


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False, connect=False)
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(title=f" Shoma mute shodid (** {member.name} **) Be dalil : ( ||**{reason}**|| ) 💀", color=0x8d0303)
    await ctx.send(embed=embed)
    embed = discord.Embed(title=f" Shoma az Server : ( **{guild.name}** ) mute shodid , Be dalil : ( **{reason}** ) 💀", color=0x8d0303)
    await member.send(embed=embed)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```ADMINISTRATOR``` دارید",
        )
        await ctx.reply(embed=embed)
#--------------------------------------mute server---------------------------------------


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server : ( ||**{ctx.guild.name}**|| ) Be Dalil ( **{reason}** ) Kick Shodid! ", color=0x5f04a3)
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar ( {member.name} ) az Server Be dalil : ( ||{reason}|| ) Kick shod!", color=0x5f04a3)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```KICK_MEMBERS``` دارید",
        )
        await ctx.reply(embed=embed)
#--------------------------------------kick server---------------------------------------


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server  : ( **||{ctx.guild.name}||** ) Ban Shodid , Be dalil : ( **{reason}** ) 💀", color=0xf10004)
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar  : ( **{member.name}** ) az Server Ban Shod , Be dalil : ( **||{reason}||** ) 💀", color=0xf10004)
    await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```BAN_MEMBERS``` دارید",
        )
        await ctx.reply(embed=embed)

#--------------------------------------ban server---------------------------------------



@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx,member: discord.Member,*,result=None):
    authorm = ctx.message.author
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description=f"Warn Be ( **{member}** ) Be Dalil ( **{result}** ) Dadeshod! :no_entry_sign:"
      )
    await ctx.reply(embed=embed)
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description = f"Shoma Tavasot ( **{authorm}** ) Be Dalil ( **{result}** ) Warn Gereftid! :no_entry_sign:"
      )
    await member.send(embed=embed)

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```ADMINISTRATOR``` دارید",
        )
        await ctx.reply(embed=embed)
#--------------------------------------warn dadan---------------------------------------




@client.command(aliases=["Clear", "CLEAR"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count="10"):
     count = int(count)
     await ctx.channel.purge(limit=count+1)
     await ctx.send(">>> "+str(count)+"Message Pak Shod")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```MANAGE_MESSAGES``` دارید",
        )
        await ctx.reply(embed=embed)
#--------------------------------------pak kardn payam ha = $clear---------------------------------------
@client.command(pass_context=True)
async def ping(ctx):
    server = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title="Ping:satellite:", description='پینگ بات: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await ctx.send(embed=embed)
    print ("Action completed: Server ping")
#--------------------------------------Ping Bot---------------------------------------
@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, input,):
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(colour=random.choice(color),description=input)
    await ctx.send(embed=embed)

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین سرور میباشد. شما نیاز به دسترسی های ```ADMINISTRATOR``` دارید",
        )
        await ctx.reply(embed=embed)
#--------------------------------------announce---------------------------------------


@client.command(aliases= ["Help", "HELP"])
async def help(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="Help")
    embed.add_field(name="<a:setting:993111639077441547> مدیریت سرور <a:setting:993111639077441547>", value=" <a:help2:993111641845674114> ```@Helpmod```", inline=True)
    embed.add_field(name="<a:help1:993111704768630836>اطلاعات حساب<a:help1:993111704768630836>", value=" <a:help2:993111641845674114> ```@Helpstats```", inline=True)
    embed.add_field(name="<a:ax:993111634048466965> تصویر <a:ax:993111634048466965>", value=" <a:help2:993111641845674114> ```@Helpimage```", inline=True)
    embed.add_field(name="🔗 اینوایت 🔗", value=" <a:help2:993111641845674114> ```@Invite```", inline=True)
    embed.add_field(name="<a:setting:993111639077441547> کامد های فان<a:setting:993111639077441547>", value=" <a:help2:993111641845674114> ```@Helpfun```", inline=True)
    await ctx.reply(embed=embed)

#--------------------------------------Help command---------------------------------------



@client.command(aliases= ["Helpstats", "HELPSTATS"])
async def helpstats(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="HelpStats")
    embed.add_field(name="🔓 اطلاعات حساب دیسکورد 🔓", value="```@User [User]```", inline=True)
    await ctx.send(embed=embed)

#--------------------------------------Help command Stats---------------------------------------

@client.command(aliases= ["Helpimage", "HELPIMAGE"])
async def helpimage(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="Helpimage")
    embed.add_field(name="پروفایل کاربر", value="```@Avatar [User]```", inline=True)
    await ctx.send(embed=embed)

#--------------------------------------Help command Stats---------------------------------------
@client.command(aliases=["Avatar", "AVATAR"])
async def avatar(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.choice(colors), timestamp=ctx.message.created_at,
                          title=f"")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Hidden Team | https://discord.gg/RRhSs4zKK4", icon_url = ctx.author.avatar_url)
    embed.set_author(name=f"آواتار کاربر به صورت زیر میباشد", icon_url = ctx.author.avatar_url)
    await ctx.reply(embed=embed)
#--------------------------------------Help command---------------------------------------
@client.command(aliases= ["Helpfun", "HELPFUN"])
async def helpfun(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="HelpFun")
    embed.add_field(name=" میزان گی بودن شما <a:help2:993111641845674114>", value="```@gay```", inline=True)
    embed.add_field(name="میزان نوب بودن شما  <a:help2:993111641845674114>", value="```@noob```", inline=True)
    embed.add_field(name="میزان جقی بودن شما <a:help2:993111641845674114>", value="```@jagh```", inline=True)
    embed.add_field(name="  8 بال <a:help2:993111641845674114>", value="```@ball```", inline=True)
    await ctx.send(embed=embed)
#--------------------------------------avatar---------------------------------------
@client.command(aliases= ["Helpmod", "HELPMOD"])
async def helpmod(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="Helpmod")
    embed.add_field(name="بن کاربر <a:setting:993111639077441547>", value="```@Ban [User] [Reason]```", inline=True)
    embed.add_field(name="کیک کاربر <a:setting:993111639077441547>", value="```@Kick [User] [Reason]```", inline=True)
    embed.add_field(name="میوت کاربر <a:setting:993111639077441547>", value="```@Mute [User] [Reason]```", inline=True)
    embed.add_field(name="آنمیوت کاربر <a:setting:993111639077441547>",value="```@Unmute [User]```", inline=True)
    embed.add_field(name="دادن اخطار به کاربر <a:setting:993111639077441547>",value="```@Warn [User] [Reason]```", inline=True)
    embed.add_field(name="پاک کردن پیام <a:setting:993111639077441547>",value="```@Clear [Number < 99]```", inline=True)
    await ctx.send(embed=embed)
#--------------------------------------Help command Mode---------------------------------------
@client.command(aliases= ["Invite", "INVITE"])
async def invite(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = random.choice(colors)
    )
    embed.add_field(name="𝑩𝒐𝒕 𝑰𝒏𝒗𝒊𝒕𝒆 :gem:", value="[***Invite-Bot***](https://discord.com/api/oauth2/authorize?client_id=980064841077243924&permissions=8&scope=bot)", inline=False)
    embed.add_field(name="𝑩𝒐𝒕 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐒𝐞𝐫𝐯𝐞𝐫 :gem:", value="[***Support-Server***](https://discord.gg/RRhSs4zKK4)", inline=False)
    embed.set_footer(text="")
    await channel.send(embed=embed)
#--------------------------------------invite dadan---------------------------------------
@tasks.loop(seconds=30)
async def main():
    images = [
            'img1.png',
            'img2.png'
            ]
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        guild = client.get_guild(905054564774973450)
        await guild.edit(banner=f.read())
#--------------------------------------Banner Chenger---------------------------------------
@client.command()
@commands.has_permissions(administrator=True)
async def botsdnd(ctx):
    activity_string = '{} servers | @help'.format(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string),status=discord.Status.dnd)
    embed = discord.Embed(colour=random.choice(color),description=f"Bot dar halet dnd hast")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def botsonline(ctx):
    activity_string = '{} servers | @help'.format(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string),status=discord.Status.online)
    embed = discord.Embed(colour=random.choice(color),description=f"Bot dar halet online hast")
    await ctx.send(embed=embed)
    

@client.command()
@commands.has_permissions(administrator=True)
async def botsidle(ctx):
    activity_string = '{} servers | @help'.format(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string),status=discord.Status.idle)
    embed = discord.Embed(colour=random.choice(color),description=f"Bot dar halet idle hast")
    await ctx.send(embed=embed)


@botsonline.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین ربات میباشد. ",
        )
        await ctx.reply(embed=embed)

@botsdnd.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین ربات میباشد. ",
        )
        await ctx.reply(embed=embed)

@botsidle.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="این دستور مختص ادمین ربات میباشد. ",
        )
        await ctx.reply(embed=embed)
#--------------------------------------stats---------------------------------------
@client.command(aliases= ["Helpowner", "help owner"])
@commands.has_permissions(administrator=True)
async def helpowner(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="owner help")
    embed.add_field(name="استاتوس بات", value="```@Help owwner stats```", inline=True)
    await ctx.send(embed=embed)
#--------------------------------------help owner id---------------------------------------
@client.command(aliases= ["Help owner stats", "help ownerstats"])
@commands.has_permissions(administrator=True)
async def helpownerstats(ctx):
    embed = discord.Embed(colour = random.choice(colors), title="owner help")
    embed.add_field(name="استاتئس انلاین", value="```@botsonline```", inline=True)
    embed.add_field(name="استاتوس ادی ان دی", value="```@botsdnd```", inline=True)
    embed.add_field(name="استاتوس ای دل", value="```@botsidle```", inline=True)
    await ctx.send(embed=embed)
#--------------------------------------Say Cmd---------------------------------------
@client.command()
async def say(ctx ,*, text: str = None):
    if text is None:
        embed1 = discord.Embed(title = "Error", description = "لطفا مسیج خود را نیز وارد کنید" , color = 0xff0000)
        await ctx.reply(embed = embed1, delete_after = 3)
        await asyncio.sleep(3)
        await ctx.message.delete()
    else:    
        await ctx.message.delete()
        embed2 = discord.Embed(description = "{0}".format(text) , color = 0x2f3136)
        await ctx.send(embed = embed2)
#--------------------------------------Salam Cmd---------------------------------------
@client.command()
async def salam(ctx ,*, text: str = None):
    if text is None:
        embed1 = discord.Embed(title = "سلام", description = "سلام رو ماهت گل " , color = 0x2ecc71)
        await ctx.reply(embed = embed1)
        await asyncio.sleep(3)

    else:    

        embed2 = discord.Embed(description = "{0}".format(text) , color = 0x2f3136)
        await ctx.send(embed = embed2)
#--------------------------------------Noob Cmd---------------------------------------
@client.command()
async def noob(ctx ,*, text: str = None):
    darsad = random.randint(0, 100)
    if text is None:
        embed1 = discord.Embed(title = "میزارن نوب بودن شما", description =  f" شما {darsad}% نوب هستید" , color = 0x2ecc71)
        await ctx.reply(embed = embed1)
        await asyncio.sleep(3)
    else:    
        await ctx.message.delete()
        embed2 = discord.Embed(description = "{0}".format(text) , color = 0x2f3136)
        await ctx.send(embed = embed2)
#--------------------------------------Gay Cmd---------------------------------------
@client.command()
async def gay(ctx ,*, text: str = None):
    darsad = random.randint(0, 100)
    if text is None: 
        embed1 = discord.Embed(title = " میزان گی بودن شما", description = f"  شما {darsad}% گی هستید" , color = 0x2ecc71)
        await ctx.reply(embed = embed1)
        await asyncio.sleep(3)
    else:    
        await ctx.message.delete()
        embed2 = discord.Embed(description = "{0}".format(text) , color = 0x2f3136)
        await ctx.send(embed = embed2)
    

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))
@client.command()
async def jagh(ctx ,*, text: str = None):
    darsad = random.randint(0, 100)
    if text is None: 
        embed1 = discord.Embed(title = " میزارن جقی بودن شما", description = f"  شما {darsad}% جقی هستید" , color = 0x2ecc71)
        await ctx.reply(embed = embed1)
        await asyncio.sleep(3)
    else:    
        await ctx.message.delete()
        embed2 = discord.Embed(description = "{0}".format(text) , color = 0x2f3136)
        await ctx.send(embed = embed2)
#--------------------------------------jagh cmd---------------------------------------
replay = ['میرم']


@client.event
async def on_message(message):
   for i in replay: 
      if i in message.content:
         await message.channel.send(f"{message.author.mention} بکیرم")
         client.dispatch('profanity', message, i)
         return 
   await client.process_commands(message)
#--------------------------------------miram cmd---------------------------------------
@client.command()
async def ball(ctx , *, q):
    URL = "https://api.parham200.ir/API/8ball"

    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            db = (data['8ball'])
            embed = discord.Embed(title=f"سوال شما : {q}",description=f"جواب : {db}",color=discord.Color.red())
            await ctx.send(embed = embed)
#--------------------------------------8ball cmd---------------------------------------
@client.event
async def on_guild_join(guild: discord.Guild):
    channel = client.get_channel(945617988806123542)
    await channel.send(embed = discord.Embed(description = "من وارد سرور شدم {}.".format(guild.name)))

@client.event
async def on_guild_remove(guild: discord.Guild):
    channel = client.get_channel(945617988806123542)
    await channel.send(embed = discord.Embed(description = "من از {} رفتم".format(guild.name)))
#--------------------------------------join or left cmd---------------------------------------s

client.run(CONFIG.TOKEN)
#--------------------------------------Login Bot---------------------------------------
# Code By AmirEdwin