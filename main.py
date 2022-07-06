import discord
import os

client = discord.Client()

prefix = "kysyinkö"
prefix2 = "kysy "
ohje = "kerro ohje"
pamaus = "putkola"
tutel = "tutel"

@client.event
async def on_ready():
  print('kysyinköö'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if(message.content.startswith(prefix)):
    await message.channel.send(message.author.mention + " kysyinkö")
    await message.delete()
    
  if(message.content.startswith(prefix2)):
    user = discord.utils.get(message.mentions)
    await message.channel.send("kysyinkö " + user.mention)
    await message.delete()

  if(message.content.startswith(ohje)):
    ohjeet = " \n kysyinkö -> kysyinkö @sinä \n kysy @joku -> kysyy siltä \n vältä typerää määrää spämmiä ettei kaadu, juusu ei jaksa resetoida jos kaatuu kokoaja"
    await message.channel.send(message.author.mention + ohjeet)
    await message.delete()

  if pamaus in message.content:
    await message.channel.send(message.author.mention + " Tässä teille putkolan pamaus")
    await message.channel.send(file=discord.File('pamaus.jpg'))

  if tutel in message.content:
    await message.channel.send(file=discord.File('tutel.mp4'))


client.run(os.getenv('TOKEN'))

print("kestääkö")