import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
     print('BOT ONLINE - OLÁ MUNDO')
     print(client.user.name)
     print(client.user.id)
     print('-----PR------')


@client.event
async def on_message(msg):
     if msg.content.startsWith('?test'):
          await client.send_message(msg.channel, 'Olá Mundo, Noxtalgic gay!')


client.run('NzEzMDQzNzg2MzIxNjI1MDg5.XsaYmA.Znp99E9gRnJ2jPY66XRLBxZK7Bc')
