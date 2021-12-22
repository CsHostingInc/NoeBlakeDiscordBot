import discord
from discord.ext import commands

TOKEN = 'OTIyNzA3NjY3OTQyNzgwOTI4.YcFYew.eu-Sj-pGW9Gh7Rv1MzFBZPCqCFU'
bot = commands.Bot(command_prefix='.',
                   description="Invite - https://discord.com/api/oauth2/authorize?client_id=922101127347073024"
                               "&permissions=8&scope=bot")
#Roles
admin = 'Discord Server Admins'

#Channels

#Staff List
Owners = 'Blake, May'
Managers = 'Mineash'
Dev = 'N/A'
Admin = 'Macro, Sachi, Mindnight'
Mod = 'N/A'
MiniMod = 'CaptionJacket'

@bot.event
async def on_ready():
    print('-----------')
    print('bot is ready')
    print(f'Logged in as - {bot.user}')
    print(f'Bot ID - {bot.user.id}')
    print('-----------')


@bot.command()
@commands.has_role(admin)
async def rules(ctx):
    await ctx.send('```Default rules:```')
    await ctx.send('1. Griefing: Griefing is when you change someone else’s builds without permission or you build within someone’s else’s house’s proximity without permission. It can also be when you break/destroy another’s build(s).')
    await ctx.send('2. Stealing: This is when you take from someone without permission.')
    await ctx.send('3. Rudeness: It’s okay to make a few jokes but don’t be overly mean and don’t be too rude when you make those jokes.')
    await ctx.send('4. Claiming stuff you shouldn’t: don’t claim stuff like landmarks, structures, and/or other people’s stuff.')
    await ctx.send('5. Killing people: don’t kill people unless you get permission to do so from the person.')
    await ctx.send('6. Chat links: Don’t send links in Discord or Minecraft chat that lead to graphic, sexual, and/or offensive content.')
    await ctx.send('7. Chat content: Don’t say anything graphic, sexual, and/or offensive in the Discord or the Minecraft chat.')
    await ctx.send('8. Illegal content: do not post, say, or send links that include illegal content.')
    await ctx.send('9. Spam: Do not post/say the same thing more than 3 times in a row or keep repeating yourself in different ways.')
    await ctx.send('10. Alt limit: do not use more than 1 alt and your main account on the server. If you’re curious this is too not use up too much data.')
    await ctx.send('11. Escaping bans or mutes: don’t use your alt to go on the server if your banned or muted.')
    await ctx.send('12. Threats: do not make threats to people on the server.')
    await ctx.send('13. Lying: do not lie to staff if you’re reported for breaking the rules.')
    await ctx.send('14. Advertising: don’t advertise any of your content or someone else’s content.  This does not include asking one or two people to do something.')
    await ctx.send('15. Don’t share info discussed with staff: if you are talking to staff, don’t share any info they tell you without asking first.')
    await ctx.send('16. Don’t share private info: do not tell your private info or someone else’s private info to anyone.')
    await ctx.send('17. Don’t hack: don’t use any hacks on the server.')
    await ctx.send('If you feel like anything should be added, anything should be edited, or anything should be deleted message me (Blake), or May (Hairy) and we will consider your suggestion.')

@bot.command()
@commands.has_role(admin)
async def staffrules(ctx):
    await ctx.send('```Staff Rules:```')
    await ctx.send('1. Do not abuse your power: don’t overuse commands, cheat, or make the game un-fun for other players.')
    await ctx.send('2. Do not make false claims: do not lie about someone breaking the rules.')
    await ctx.send('3. Ask before making major changes: always ask before doing anything that could change a lot of stuff. The person to ask would either be me (Blake) or May (Hairy).')
    await ctx.send('4. Don’t share private staff info: don’t share info that is only for staff.')
    await ctx.send('5. Don’t edit any code: if you have access to code, don’t mess with it without permission. This rule does not apply to developers.')
    await ctx.send('6. Follow other rules: follow the default rules. ')




@bot.command()
@commands.has_role(admin)
async def stafflist(ctx):
    embed = discord.Embed(title="Minecraft Server Staff List", description="All of our friendly staff",
                          color=0x00ff00)
    embed.add_field(name="Owners", value=f'{Owners}', inline=False)
    embed.add_field(name='Manager', value=f'{Managers}', inline=False)
    embed.add_field(name='Dev', value=f'{Dev}', inline=False)
    embed.add_field(name='Admin', value=f'{Admin}', inline=False)
    embed.add_field(name='Mod', value=f'{Mod}', inline=False)
    embed.add_field(name='MiniMod', value=f'{MiniMod}', inline=False)
    embed.set_footer(text='©CsHosting 2021')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(admin)
async def mcvote(ctx):
    embed = discord.Embed(title="NeoBlake Vote", description="Please vote for our Minecraft Sever, Click 'NeoBlake Vote'",
                          color=0x00ff00, url='https://minecraft-server-list.com/server/484121/')
    embed.set_footer(text='©CsHosting 2021')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(admin)
async def disvote(ctx):
    embed = discord.Embed(title="NeoBlake Discord Vote", description="Please vote for our Discord Sever, Click 'NeoBlake Discord Vote'",
                          color=0x00ff00, url='https://discord.st/server/neoblake/')
    embed.set_footer(text='©CsHosting 2021')
    await ctx.send(embed=embed)

bot.run(TOKEN)

