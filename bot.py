import discord
import asyncio
import random
import os

client = discord.Client()
dr=os.getcwd()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Crusader Kings II'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('{test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'calculating messages')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'you have {} messages'.format(counter))
    elif message.content.startswith ('{help'):
        await client.send_message(message.channel, 'commands: `{test`, `{snooze`, `{lmdo`, `{szcz`, `{smug`, `{sacroni`, `{say`')
    elif message.content.startswith('{snooze'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'done snoozing')
    elif message.content.startswith('{lmdo'):
        await client.send_message(message.channel, 'Lmdo')
    elif message.content.startswith ('{szcz'):
        szczs = open(dr + "\\szcz.txt", "r")
        szczlist = szczs.readlines()
        await client.send_message(message.channel, random.choice(szczlist))
    elif message.content.startswith ('{smug'):
        smug = os.listdir(dr + "\\smug")
        smug.remove('Thumbs.db')
        await client.send_file(message.channel, dr + '\\smug\\' + random.choice(smug))
    elif message.content.startswith ('{sacroni'):
        sacroni = os.listdir(dr + "\\sacroni")
        sacroni.remove('Thumbs.db')
        await client.send_file(message.channel, dr + '\\sacroni\\' + random.choice(sacroni))
    elif message.content.startswith ('{say'):
        say = message.content[len('{say'):].strip()
        if say != '':
            if message.author.bot == True:
                await client.send_message(message.channel, "pwned kiddo")
            else:
                await client.send_message(message.channel, say)


client.run('MjQ4ODc4MTY5NzA3MjQ5Njc0.Cw-J2w.e8ebHynG1fd3WnCV8JSn5O6CPBs')
