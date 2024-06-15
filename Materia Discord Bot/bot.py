import discord
import time
import json
from urllib.request import Request, urlopen

def callUniversalisApi(world, itemID):
    link = "https://universalis.app/api/" + str(world) + "/" + str(itemID) #+ "?hq=NQ"
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    jsonListOfItems = urlopen(req).read().decode("utf-8")
    return jsonListOfItems

def getAllAuctions(world, itemID, quality):
    jsonList = getJsonObj(world, itemID, quality)
    jsonObject = json.loads(jsonList)
    numOfPosts = len(jsonObject["listings"])
    listOfImportantInfo = []
    for x in range(numOfPosts):
        retainerName = str(jsonObject["listings"][x]["retainerName"])
        quantity = str(jsonObject["listings"][x]["quantity"])
        pricePerUnit = str(jsonObject["listings"][x]["pricePerUnit"])
        listOfImportantInfo.append([retainerName, quantity, pricePerUnit])
    return listOfImportantInfo

def getLowestPrice(world, itemid, quality):
    itemList = getAllAuctions(world, itemid, quality)
    min = 99999999999999
    for x in itemList:
        if int(x[2]) < int(min):
            min = x[2]
    return min, itemList # CHANGE TO RETURN ITEMLIST - THIS WAS CHANGED FOR MATERIA, REMOVE ITEMLIST TO UNBREAK FOR DISCORD

def getJsonObj(world, itemID, quality):
    qualityTxt = ""
    if quality.lower().strip() == "hq":
        qualityTxt = "?hq=true"
    elif quality.lower().strip() == "nq":
        qualityTxt = "?hq=false"
    link = "https://universalis.app/api/" + str(world) + "/" + str(itemID) + qualityTxt
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    jsonListOfItems = urlopen(req).read().decode("utf-8")
    return jsonListOfItems

def BuyThresholdList(world,quantityLimit):
    lines = open("materiaBuyList.txt", "r").readlines()
    buyList = []
    for x in lines:
        temp = x.split(",")
        itemname = temp[0]
        if itemname != "#ItemName":
            itemid = temp[1]
            itemqual = temp[2]
            itemprice = temp[3].strip()
            tempname = itemname.strip()
            low, listOfItems = getLowestPrice(world, int(itemid), itemqual)
            if int(low) <= int(itemprice):
                quantityOfBuyable = 0
                for y in listOfItems:
                    if int(y[2]) < int(itemprice):
                        quantityOfBuyable += int(y[1])
                if int(quantityOfBuyable) > int(quantityLimit):
                    qty = "Qty: " + str(quantityOfBuyable)
                    if len(str(quantityOfBuyable)) == 1:
                        qty += "    "
                    elif len(str(quantityOfBuyable)) == 2:
                        qty += "   "
                    else:
                        qty += " "
                    buyList.append("`"+qty + "Price:" + str(low) + "\t" + tempname+"`")
    return buyList

async def MateriaSearch(w,message,quantityLimit):
    buyList = []
    try:
        buyList = BuyThresholdList(w,quantityLimit)
    except Exception as e:
        #print(e)
        try:
            buyList = BuyThresholdList(w,quantityLimit)
        except:
            x = ""  # A 2nd error connecting occurred.
    editMsg = "> ### "+w+"\n"
    for x in buyList:
        editMsg += x + "\n"
    await message.edit(content=editMsg)


async def MateriaSearchByWorld(channel):
    Ultros = await channel.send("> ### Ultros\nMateria finds will go here.")
    Behemoth = await channel.send("> ### Behemoth\nMateria finds will go here.")
    Excalibur = await channel.send("> ### Excalibur\nMateria finds will go here.")
    Exodus = await channel.send("> ### Exodus\nMateria finds will go here.")
    Famfrit = await channel.send("> ### Famfrit\nMateria finds will go here.")
    Hyperion = await channel.send("> ### Hyperion\nMateria finds will go here.")
    Lamia = await channel.send("> ### Lamia\nMateria finds will go here.")
    Leviathan = await channel.send("> ### Leviathan\nMateria finds will go here.")

    # Change minimum quantity to cause an edited message.
    quantityLimit = 30

    while True:
        await MateriaSearch("Ultros",Ultros,quantityLimit)
        await MateriaSearch("Behemoth",Behemoth,quantityLimit)
        await MateriaSearch("Excalibur",Excalibur,quantityLimit)
        await MateriaSearch("Exodus",Exodus,quantityLimit)
        await MateriaSearch("Famfrit",Famfrit,quantityLimit)
        await MateriaSearch("Hyperion",Hyperion,quantityLimit)
        await MateriaSearch("Lamia",Lamia,quantityLimit)
        await MateriaSearch("Leviathan",Leviathan,quantityLimit)
        print("Sleepy time.")
        time.sleep(30)

def run_discord_bot():
    TOKEN = 'REPLACE ME WITH REAL TOKEN'
    client = discord.Client(intents=discord.Intents.all())
    @client.event
    async def on_ready():
        # Materia
        materia_sell_primal = client.get_channel(1244017021021196359)
        materia_sell_aether = client.get_channel(1244017050515669023)
        materia_sell_crystal = client.get_channel(1244017070727761945)
        materia_sell_dynamis = client.get_channel(1244017083235176459)
        await materia_sell_primal.purge()
        await MateriaSearchByWorld(materia_sell_primal)

    @client.event
    async def on_message(message):
        if (message.content == "Chris sucks"):
            await message.channel.send("Truuuuu")

    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()
    pass