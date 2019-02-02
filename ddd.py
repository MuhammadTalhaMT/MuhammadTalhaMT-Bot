import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='!help for commands'))
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello! Welcome to the server of MuhammadTalhaMT, have a nice stay with us! Please DM MuhammadTalhaMT#7530 to invite your bot to this server.')
    print('Sent message to ' + member.name)
    
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name ='Bot owners or public members')
    await client.addroles(member, role)

@client.event
async def on_message(message):
    if message.content == '!help':
        await client.send_message(message.channel,'''
Commands:
!help
(Get commands)
!cat
(Get a random cat photo)
!Emergency
(THIS IS FAKE, use for fun only. Try it.
!memes
(Time for a Meme)
!ping
(Get your ping now!)
!servertimings
(Get the server timings shudule)
!flipcoin
(You got Heads or Tails)''')
                                                          
               
    if message.content == 'How are you Bot?':
        await client.send_message(message.channel,'I am fine, you?')
    if message.content == '!Emergency':
        await client.send_message(message.channel,'Why are you saying me, call 911 for emergency! Your thinking like you called 911.')
    if message.content == '!YoutubeChannelName':
        await client.send_message(message.channel,'MuhammadTalhaMT')
    if message.content == '!memes':
        em = discord.Embed(description='Really?!')
        randomlist = ['https://images-ext-2.discordapp.net/external/8V8xOE2qdMZdxedfiwqm7xIuhosC97Lwje6e-7kr29c/%3Fwidth%3D400%26height%3D300/https/media.discordapp.net/attachments/540533802536140813/540864408373559297/what-is-a-meme.png','https://media.discordapp.net/attachments/540533802536140813/540864768500695066/2018-09-11-image-34.png?width=400&height=225']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!ping'):
        randomlist = ['Pong (100)','Pong (50)','Pong (141)','Pong (30)']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!servertimings':
        await client.send_message(message.channel,'Server is closed in night and opened in morning! But 24 HOURS on holidays.')
    if message.content == 'Good.':
        await client.send_message(message.channel,'Nice!')
    if message.content.startswith('!flipcoin'):
        randomlist = ['Heads','Tails']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!credits'):
        await client.send_message(message.channel,'<@%s> Credits goes to <@429567943995686912>'  %(message.author.id))
    if message.content == '!cat':
        em = discord.Embed(description='Chill')
        em.set_image(url='https://media.discordapp.net/attachments/533305003364974594/540907947887165461/02-cat-training-NationalGeographic_1484324.ngsversion.1526587209178.adapt.1900.1.jpg?width=400&height=267')
        await client.send_message(message.channel, embed=em)
    if ('hack') in message.content:
       await client.delete_message(message)
client.run('NTQwNTEwOTgxNjkyODUwMTc2.DzYLFg.hK47nk8vXuuKY-OiXhHAiFo9ZCk')
