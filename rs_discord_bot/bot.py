import discord, requests as rq, re
import utilities as rsu

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #Events commented out as the output is far too large.
    #if message.content.startswith("$events"):
    #    player = re.match('\$events (.*)',message.content).group(1)
    #    events = rsu.eventscrape(player)
    #    if events == "Error":
    #        await message.channel.send(f'An error occurred, does that player exist?')
    #    else:
    #        new_message = []
    #        for i in events:
    #            new_message.append(f'{i[0]} - {i[1]}: {i[2]}')
    #        await message.channel.send('\n'.join(new_message))
    if message.content.startswith('$quests'):
        player = re.match('\$quests (.*)',message.content).group(1)
        quests = rsu.apiscrape(player)
        if quests == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        else:
            await message.channel.send(f'{player} has completed {quests[6]} out of {quests[6] + quests[7] + quests[8]} quests. {player} has started {quests[8]} out of {quests[6] + quests[7] + quests[8]} quests. {player} has not yet started {quests[7]} out of {quests[6] + quests[7] + quests[8]} quests.')
    elif message.content.startswith('$combat'):
        player = re.match('\$combat (.*)',message.content).group(1)
        combat = rsu.combat(player)
        if combat == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        else:
            await message.channel.send(f'{player} is combat level {combat}.')
    elif message.content.startswith('$totalskill'):
        player = re.match('\$totalskill (.*)',message.content).group(1)
        totalskill = rsu.totalskill(player)
        if totalskill == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        else:
            await message.channel.send(f'{player} is at total skill level {totalskill}.')
    elif message.content.startswith('$totalxp'):
        player = re.match('\$totalxp (.*)',message.content).group(1)
        totalxp = rsu.totalxp(player)
        if totalxp == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        else:
            await message.channel.send(f'{player} is at total XP {"{:,}".format(totalxp)}.')
    elif message.content.startswith('$rank'):
        player = re.match('\$rank (.*)',message.content).group(1)
        rank = rsu.rank(player)
        if rank == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        else:
            await message.channel.send(f'{player} is ranked {rank}.')
    elif message.content.startswith('$maxlevels'):
        player = re.match('\$maxlevels (.*)',message.content).group(1)
        maxlevels = rsu.maxcape(player)
        if maxlevels == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        elif maxlevels == 0:
            await message.channel.send(f'{player} has unlocked the Max Cape! Congratulations!')
        else:
            await message.channel.send(f'{player} needs {"{:,}".format(maxlevels)} levels to unlock the Max Cape.')
    elif message.content.startswith('$maxxp'):
        player = re.match('\$maxxp (.*)',message.content).group(1)
        maxxp = rsu.maxxp(player)
        if maxxp == "Error":
            await message.channel.send(f'An error occurred, does that player exist?')
        elif maxxp == 0:
            await message.channel.send(f'{player} has unlocked the Max Cape! Congratulations!')
        else:
            await message.channel.send(f'{player} needs {"{:,}".format(round(maxxp,2))} XP to unlock the Max Cape.')
    elif message.content.startswith('$hi bot'):
        await message.channel.send(f'Hello @{message.author}!')

with open('discord_bot_token.txt','r') as fhand:
    token = fhand.read().strip()
client.run(token)