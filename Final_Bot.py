import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server


@client.event
async def on_message(message):

    

    if message.content == ",gchoose":
        if "441137252664475649" in [role.id for role in message.author.roles]:
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!givekeys <" + myline + "> 1 **You won the giveaway!**"
            await client.send_message(message.channel, msg)
            os.remove("giveaway.txt")
            #clear text file here



    
    elif message.content == ",gstart": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = 'Giveaway starting now! Type `,apple` to enter. Ending in 30 seconds @here'.format(message)
            await client.send_message(message.channel, msg)
            file = open("giveaway.txt","a")
       
   


        
    elif message.content == (',apple'):
        if ("@" + message.author.id) not in open("giveaway.txt").read():
            file = open("giveaway.txt", "a")
            file.write("@" + message.author.id + "\n") #message.author.id
            await client.send_message(message.author, '**You have been entered into the giveaway, goodluck**')

    elif message.content.startswith(",add"):
        if "479719598724218920" in [role.id for role in message.author.roles]:
            splitted = message.content.split()
            global word
            word = splitted[1]
            file = open(word + ".txt", "w")
            length = len(word)
            file.write(message.content[len(word)+5:])
            file.close()
            await client.send_message(message.channel, "**Added ** `" + message.content[len(word)+5:] + "` ** to the keyword: ** `" + word + "`")
            await client.delete_message(message)        
        
















    
    elif message.content.startswith("," + message.content.replace(",", "")): #get a role soon
        global keyword
        keyword = message.content.replace(",", "") #how many characters in keyword
        file = open(keyword + ".txt", "r")
        await client.send_message(message.channel, file.read())
        await client.delete_message(message)


            
client.run("NDc5MzAzMDIyMzI1NzkyNzc4.DlXt4w.jrxpFxbC6v9POH0MlDmx_I2hHJ0") #Replace token with your bots token
