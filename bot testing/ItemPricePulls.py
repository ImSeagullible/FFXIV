import json
from urllib.request import Request, urlopen
import time

startTime = time.time()

primal = ["Behemoth","Excalibur","Exodus","Famfrit","Hyperion","Lamia","Leviathan","Ultros"]
aether = ["Adamantoise","Cactuar","Faerie","Gilgamesh","Midgardsormr","Sargatanas","Siren"]
crystal = ["Balmung","Brynhildr","Coeurl","Diabolos","Goblin","Malboro","Mateus","Zalera"]
dynamis = ["Halicarnassus","Maduin","Marilith","Seraph"]
materiaFilters = ("?entries=0"
                  "&statsWithin=0"
                  "&entriesWithin=0&"
                  "fields=items.listings.pricePerUnit%2C+"
                  "items.listings.worldName%2C+"
                  "items.listings.hq%2C+"
                  "items.listings.quantity")

def createWorldMateria(worldName, materia):
    worldMateria = []
    for x in materia:
        materiaToAdd = []
        for y in x[3]:
            if y[3] == worldName:
                append = True
                for z in materiaToAdd:
                    if z[0] == y[0] and z[2] == y[2]:
                        z[1] = int(z[1]) + int(y[1])
                        append = False
                if append:
                    materiaToAdd.append([y[0], y[1], y[2]])

        if len(materiaToAdd) > 0:
            worldMateria.append([x[0], x[1], x[2], worldName, x[5], materiaToAdd])
    return worldMateria

def write_materia_to_file(world_materia):
    #with open(f"Materia/{world_name}/materia.txt", "w") as f:
    with open(f"allWorldMateria.txt", "a") as f:
        for x in world_materia:
            f.write("~" + x[0] + "," + x[1] + "," + x[2] + "," + x[3] + "," + x[4] + "\n")
            for y in x[5]:
                f.write(str(y[0]) + "," + str(y[1]) + "," + y[2] + "\n")

def doTheThings():
    f = open("materiaBuyList.txt", "r")
    materiaBuyList = f.readlines()
    f.close()

    materia = []
    materiaItemIDs = []

    for x in materiaBuyList:
        temp = x.split(",")
        itemName = temp[0]
        itemID = temp[1]
        itemPrice = temp[2]
        hq = temp[3]
        qtyLimit = temp[4].strip()
        if itemName != "#ItemName":
            materiaItemIDs.append(temp[1])
            materia.append([itemName, itemID, itemPrice, [], hq, qtyLimit])

    northAmericanMateriaAPI = "https://universalis.app/api/v2/North-America/" + ",".join(materiaItemIDs) + materiaFilters
    itemReturn = json.loads(urlopen(Request(northAmericanMateriaAPI, headers={'User-Agent': 'Mozilla/5.0'})).read().decode("utf-8"))

    items = itemReturn["items"]
    listingsToAdd = []
    for x in materiaItemIDs:
        for y in range(len(items[str(x)]["listings"])):
            quantity = str(items[str(x)]["listings"][y]["quantity"])
            world = str(items[str(x)]["listings"][y]["worldName"])
            pricePerItem = str(items[str(x)]["listings"][y]["pricePerUnit"])
            hq = str(items[str(x)]["listings"][y]["hq"])
            for z in materia:
                if x == z[1] and int(pricePerItem) <= int(z[2]) and (z[4] == "any" or z[4] == str(hq.lower())):
                    listingsToAdd.append([pricePerItem,quantity,hq,world])
        for z in materia:
            if x == z[1]:
                z[3] = listingsToAdd
        listingsToAdd = []

    # Erase file
    open(f"allWorldMateria.txt", "w").close()

    # Primal
    behemothMateria = createWorldMateria("Behemoth", materia)
    excaliburMateria = createWorldMateria("Excalibur", materia)
    exodusMateria = createWorldMateria("Exodus", materia)
    famfritMateria = createWorldMateria("Famfrit", materia)
    hyperionMateria = createWorldMateria("Hyperion", materia)
    lamiaMateria = createWorldMateria("Lamia", materia)
    leviathanMateria = createWorldMateria("Leviathan", materia)
    ultrosMateria = createWorldMateria("Ultros", materia)

    write_materia_to_file(behemothMateria)
    write_materia_to_file(excaliburMateria)
    write_materia_to_file(exodusMateria)
    write_materia_to_file(famfritMateria)
    write_materia_to_file(hyperionMateria)
    write_materia_to_file(lamiaMateria)
    write_materia_to_file(leviathanMateria)
    write_materia_to_file(ultrosMateria)

    # Aether
    adamantoiseMateria = createWorldMateria("Adamantoise", materia)
    cactuarMateria = createWorldMateria("Cactuar", materia)
    faerieMateria = createWorldMateria("Faerie", materia)
    gilgameshMateria = createWorldMateria("Gilgamesh", materia)
    jenovaMateria = createWorldMateria("Jenova", materia)
    midgardsormrMateria = createWorldMateria("Midgardsormr", materia)
    sargatanasMateria = createWorldMateria("Sargatanas", materia)
    sirenMateria = createWorldMateria("Siren", materia)

    write_materia_to_file(adamantoiseMateria)
    write_materia_to_file(cactuarMateria)
    write_materia_to_file(faerieMateria)
    write_materia_to_file(gilgameshMateria)
    write_materia_to_file(jenovaMateria)
    write_materia_to_file(midgardsormrMateria)
    write_materia_to_file(sargatanasMateria)
    write_materia_to_file(sirenMateria)

    # Crystal
    balmungMateria = createWorldMateria("Balmung", materia)
    brynhildrMateria = createWorldMateria("Brynhildr", materia)
    coeurlMateria = createWorldMateria("Coeurl", materia)
    diabolosMateria = createWorldMateria("Diabolos", materia)
    goblinMateria = createWorldMateria("Goblin", materia)
    malboroMateria = createWorldMateria("Malboro", materia)
    mateusMateria = createWorldMateria("Mateus", materia)
    zaleraMateria = createWorldMateria("Zalera", materia)

    write_materia_to_file(balmungMateria)
    write_materia_to_file(brynhildrMateria)
    write_materia_to_file(coeurlMateria)
    write_materia_to_file(diabolosMateria)
    write_materia_to_file(goblinMateria)
    write_materia_to_file(malboroMateria)
    write_materia_to_file(mateusMateria)
    write_materia_to_file(zaleraMateria)

    # Dynamis
    halicarnassusMateria = createWorldMateria("Halicarnassus", materia)
    maduinMateria = createWorldMateria("Maduin", materia)
    marilithMateria = createWorldMateria("Marilith", materia)
    seraphMateria = createWorldMateria("Seraph", materia)

    write_materia_to_file(halicarnassusMateria)
    write_materia_to_file(maduinMateria)
    write_materia_to_file(marilithMateria)
    write_materia_to_file(seraphMateria)


    #endTime = time.time()
    #totalTime = endTime - startTime
    #print(totalTime)


if __name__ == '__main__':
    while True:
        try:
            doTheThings()
            print("Data pulled. Going again in 60 seconds.")
        except Exception as e:
            print("Trying again in 60sec: Somethin' fucked up.\n" + e)

        time.sleep(60)
    pass