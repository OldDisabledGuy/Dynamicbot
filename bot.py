import discord
import asyncio
import random

client = discord.Client()

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
        await client.send_message(message.channel, 'commands: `{test`, `{sleep`, `{lmdo`, `{szcz`')
    elif message.content.startswith('{sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'done sleeping')
    elif message.content.startswith('{lmdo'):
        await client.send_message(message.channel, 'Lmdo')
    elif message.content.startswith ('{szcz'):
        szcz = ['szczur', 'szczupak', 'chrząszcz', 'szczecin', 'szczebrzeszyn', 'szczerość', 'szczekać', 'szczęka', "pszczoła", 'oszczędzać', 'płaszcz', 'szczegóły', 'puszcza', 'paszcza', 'chińszczyzna', 'polszczyzna', 'barszcz', 'szczeniak', 'szczep', 'szczyt']
        await client.send_message(message.channel, random.choice(szcz))

client.run('MjQ4ODc4MTY5NzA3MjQ5Njc0.Cw-J2w.e8ebHynG1fd3WnCV8JSn5O6CPBs')
