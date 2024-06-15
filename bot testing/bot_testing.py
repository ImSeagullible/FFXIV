import asyncio

import discord
import time
import json
from datetime import datetime
from urllib.request import Request, urlopen

from discord.ext import tasks


async def messageUpdate(world, message):
    f = open("allWorldMateria.txt", "r")
    lines = f.readlines()
    f.close()

    itemName = ""
    itemID = ""
    threshold = ""
    price = ""
    quantity = ""
    quantityThreshold = 0
    quality = ""
    pulledWorld = ""
    itemsList  = []
    checkItem = False

    for x in lines:
        temp = x.split(",")

        if temp[0][0:1] == "~" and world == temp[3].strip():
            itemName = temp[0][1:]
            itemID = temp[1]
            threshold = temp[2]
            quantityThreshold = int(temp[4])
            checkItem = True
        elif temp[0][0:1] == "~" and world != temp[3].strip():
            checkItem = False
        elif temp[0][0:1] != "~" and checkItem == True:
            price = temp[0]
            quantity = temp[1].strip()
            if temp[2] == "False":
                quality = "NQ"
            else:
                quality = "HQ"
            itemsList.append([itemName, itemID, threshold, price, quantity, quality, quantityThreshold])

    itemName = ""
    formattedItemList = []
    for x in itemsList:
        if x[0] != itemName:
            itemName = x[0]
            threshold = x[2]
            priceAverage = 0
            quantityTotal = 0
            quality = x[5]
            quantityThreshold = x[6]
            for y in itemsList:
                if y[0] == itemName:
                    priceAverage += int(y[3]) * int(y[4])
                    quantityTotal += int(y[4])

            priceAverage = int((priceAverage / quantityTotal))
            if quantityTotal >= quantityThreshold:
                formattedItemList.append("`" + str(itemName) + " || Avg: " + str(priceAverage) + " || Qty: " + str(quantityTotal) + "`")
    editMessage = "> ### " + world + "\n"
    for x in formattedItemList:
        editMessage += x + "\n"
    await message.edit(content=editMessage)



async def primalMateriaInitialize(channel):
    await channel.purge()
    Ultros = await channel.send("> ### Ultros\nMateria finds will go here.")
    Behemoth = await channel.send("> ### Behemoth\nMateria finds will go here.")
    Excalibur = await channel.send("> ### Excalibur\nMateria finds will go here.")
    Exodus = await channel.send("> ### Exodus\nMateria finds will go here.")
    Famfrit = await channel.send("> ### Famfrit\nMateria finds will go here.")
    Hyperion = await channel.send("> ### Hyperion\nMateria finds will go here.")
    Lamia = await channel.send("> ### Lamia\nMateria finds will go here.")
    Leviathan = await channel.send("> ### Leviathan\nMateria finds will go here.")

    # Change minimum quantity to cause an edited message.
    quantityLimit = 30 # this isnt implemented :(
    primalMateriaUpdate.start(Ultros, Behemoth, Excalibur, Exodus, Famfrit, Hyperion, Lamia, Leviathan)

@tasks.loop(seconds=60)
async def primalMateriaUpdate(Ultros, Behemoth, Excalibur, Exodus, Famfrit, Hyperion, Lamia, Leviathan):
    await messageUpdate("Ultros", Ultros)
    await messageUpdate("Behemoth", Behemoth)
    await messageUpdate("Excalibur", Excalibur)
    await messageUpdate("Exodus", Exodus)
    await messageUpdate("Famfrit", Famfrit)
    await messageUpdate("Hyperion", Hyperion)
    await messageUpdate("Lamia", Lamia)
    await messageUpdate("Leviathan", Leviathan)

async def aetherMateriaInitialize(channel):
    await channel.purge()
    Adamantoise = await channel.send("> ### Adamantoise\nMateria finds will go here.")
    Cactuar = await channel.send("> ### Cactuar\nMateria finds will go here.")
    Faerie = await channel.send("> ### Faerie\nMateria finds will go here.")
    Gilgamesh = await channel.send("> ### Gilgamesh\nMateria finds will go here.")
    Jenova = await channel.send("> ### Jenova\nMateria finds will go here.")
    Midgardsormr = await channel.send("> ### Midgardsormr\nMateria finds will go here.")
    Sargatanas = await channel.send("> ### Sargatanas\nMateria finds will go here.")
    Siren = await channel.send("> ### Siren\nMateria finds will go here.")

    # Change minimum quantity to cause an edited message.
    quantityLimit = 30 # this isnt implemented :(
    aetherMateriaUpdate.start(Adamantoise, Cactuar, Faerie, Gilgamesh, Jenova, Midgardsormr, Sargatanas, Siren)

@tasks.loop(seconds=60)
async def aetherMateriaUpdate(Adamantoise, Cactuar, Faerie, Gilgamesh, Jenova, Midgardsormr, Sargatanas, Siren):
    await messageUpdate("Adamantoise", Adamantoise)
    await messageUpdate("Cactuar", Cactuar)
    await messageUpdate("Faerie", Faerie)
    await messageUpdate("Gilgamesh", Gilgamesh)
    await messageUpdate("Jenova", Jenova)
    await messageUpdate("Midgardsormr", Midgardsormr)
    await messageUpdate("Sargatanas", Sargatanas)
    await messageUpdate("Siren", Siren)

async def crystalMateriaInitialize(channel):
    await channel.purge()
    Balmung = await channel.send("> ### Balmung\nMateria finds will go here.")
    Brynhildr = await channel.send("> ### Brynhildr\nMateria finds will go here.")
    Coeurl = await channel.send("> ### Coeurl\nMateria finds will go here.")
    Diabolos = await channel.send("> ### Diabolos\nMateria finds will go here.")
    Goblin = await channel.send("> ### Goblin\nMateria finds will go here.")
    Malboro = await channel.send("> ### Malboro\nMateria finds will go here.")
    Mateus = await channel.send("> ### Mateus\nMateria finds will go here.")
    Zalera = await channel.send("> ### Zalera\nMateria finds will go here.")

    # Change minimum quantity to cause an edited message.
    quantityLimit = 30 # this isnt implemented :(
    crystalMateriaUpdate.start(Balmung, Brynhildr, Coeurl, Diabolos, Goblin, Malboro, Mateus, Zalera)

@tasks.loop(seconds=60)
async def crystalMateriaUpdate(Balmung, Brynhildr, Coeurl, Diabolos, Goblin, Malboro, Mateus, Zalera):
    await messageUpdate("Balmung", Balmung)
    await messageUpdate("Brynhildr", Brynhildr)
    await messageUpdate("Coeurl", Coeurl)
    await messageUpdate("Diabolos", Diabolos)
    await messageUpdate("Goblin", Goblin)
    await messageUpdate("Malboro", Malboro)
    await messageUpdate("Mateus", Mateus)
    await messageUpdate("Zalera", Zalera)

async def dynamisMateriaInitialize(channel):
    await channel.purge()
    Halicarnassus = await channel.send("> ### Halicarnassus\nMateria finds will go here.")
    Maduin = await channel.send("> ### Maduin\nMateria finds will go here.")
    Marilith = await channel.send("> ### Marilith\nMateria finds will go here.")
    Seraph = await channel.send("> ### Seraph\nMateria finds will go here.")

    # Change minimum quantity to cause an edited message.
    quantityLimit = 30 # this isnt implemented :(
    dynamisMateriaUpdate.start(Halicarnassus, Maduin, Marilith, Seraph)

@tasks.loop(seconds=60)
async def dynamisMateriaUpdate(Halicarnassus, Maduin, Marilith, Seraph):
    await messageUpdate("Halicarnassus", Halicarnassus)
    await messageUpdate("Maduin", Maduin)
    await messageUpdate("Marilith", Marilith)
    await messageUpdate("Seraph", Seraph)

def add_to_item_list(name, itemID, quality, quantity, buyThreshold, sellThreshold):
    #TO-DO, check if item already exists.
    #Run an example API get item to make sure it's valid.

    f = open("itemlist.txt", "a")
    f.write(name + "," + itemID + "," + quality + "," + quantity + "," + buyThreshold + "," + sellThreshold + "\n")
    f.close()

def run_discord_bot():
    TOKEN = 'REPLACE ME WITH REAL TOKEN'
    client = discord.Client(intents=discord.Intents.all())

    @tasks.loop(seconds=30)
    @client.event
    async def on_ready():
        # Item Channels
        item_sell_ultros = client.get_channel(1229224217191518258)
        item_buy_ultros = client.get_channel(1229223975205343273)
        item_buy_primal = client.get_channel(1229224542069723136)
        item_buy_aether = client.get_channel(1244017050515669023)
        item_buy_crystal = client.get_channel(1244017070727761945)
        item_buy_dynamis = client.get_channel(1244017083235176459)

        # Materia Channels
        materia_buy_primal = client.get_channel(1244017021021196359)
        materia_buy_aether = client.get_channel(1244017050515669023)
        materia_buy_crystal = client.get_channel(1244017070727761945)
        materia_buy_dynamis = client.get_channel(1244017083235176459)

        #other
        dawntrailtest = client.get_channel(1229202549471580253)
        bot_info = client.get_channel(1229209368847847515)
        await bot_info.send("Started up at: " + str(datetime.now()))

        await primalMateriaInitialize(materia_buy_primal)
        await aetherMateriaInitialize(materia_buy_aether)
        await crystalMateriaInitialize(materia_buy_crystal)
        await dynamisMateriaInitialize(materia_buy_dynamis)

    @client.event
    async def on_message(message):
        if message.content == "Chris sucks":
            await message.channel.send("Truuuuu")
        elif message.content == "!chris":
            await message.channel.send("sucks")
        elif message.content == "!purge":
            await message.channel.purge()
        elif (message.content == "!commands" or message.content == "!help"
              and (str(message.channel) == "general" or str(message.channel) == "bot-info"
                   or str(message.channel) == "list-management" or str(message.channel) == "dawntrailtest")):
            await message.channel.send("!help / !commands - Returns a list of commands\n\n"
                "!channels - Returns a list of what Channels this bot has visibility to\n\n"
                "!purge - Purges the last ~100 messages in the channel this was sent in\n\n"
                "!checklist - Returns a list of items currently tracked\n\n"
                "!edititem - Edits an item in the list\n\n"
                "!additem - Adds an item to the list.\n"
                                       "- Expected input is a comma separated string with the following format:\n"
                                       " - name, itemID, quality, quantity, buyThreshold, sellThreshold\n"
                                       "- ItemID can be obtained from the URL after searching it here: https://universalis.app/\n"
                                       "- The name is just for reference. It does not have to be the exact name, the ItemID is what I search by.\n"
                                       "- Quantity is how many of an item must be under the BuyThreshold before it alerts. So you don't go look for only 1 item if it's potions.\n"
                                       "- Example: !additem Wild Sage, 33150, hq/lq/any, 1, 5000, 15000\n"
                "\n!removeitem - Removes an item from the list\n\n"
                "!clearlist - Clears the list\n\n"
                "!stopalerts - Stops the bot from pinging you in all channels\n\n"
                "!startalerts - Starts the bot pinging you in all channels\n\n"
                "!chris\n")
        elif str(message.content).startswith("!additem") and str(message.channel) == "list-management":
            messageStr = str(message.content)
            if len(messageStr.split(",")) == 6:
                if messageStr.split(",")[2].lower().strip() in ["hq", "lq", "any"]:
                    if messageStr.split(",")[1].strip().isdigit() and messageStr.split(",")[3].strip().isdigit() and messageStr.split(",")[4].strip().isdigit() and messageStr.split(",")[5].strip().isdigit():
                        add_to_item_list(messageStr.split(",")[0][9:], messageStr.split(",")[1].strip(), messageStr.split(",")[2].strip(), messageStr.split(",")[3].strip(), messageStr.split(",")[4].strip(), messageStr.split(",")[5].strip())
                        await message.channel.send("Item added.")
                    else:
                        await message.channel.send("Invalid input, itemID, quantity, buyThreshold, and sellThreshold must be integers.")
                else:
                    await message.channel.send("Invalid input, quality did not match to one of the following: hq, lq, any.")
            else:
                await message.channel.send("Invalid input, did not find 5 sections in the message.")


    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()
    pass