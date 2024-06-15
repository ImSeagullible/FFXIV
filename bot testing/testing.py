f = open("allWorldMateria.txt", "r")
lines = f.readlines()
f.close()

world = "Ultros"

itemName = ""
itemID = ""
threshold = ""
price = ""
quantity = ""
quality = ""
pulledWorld = ""
itemsList = []
for x in lines:
    temp = x.split(",")
    if temp[0][0:1] == "~" and world == temp[3].strip():
        itemName = temp[0][1:]
        itemID = temp[1]
        threshold = temp[2]
        pulledWorld = temp[3].strip()
        print(itemName, itemID, threshold, world, pulledWorld)
    elif temp[0][0:1] != "~" and world == pulledWorld:
        print("in not ~")
        price = temp[0]
        quantity = temp[1]
        if temp[2] == "False":
            quality = "NQ"
        else:
            quality = "HQ"
        itemsList.append([itemName, itemID, threshold, price, quantity, quality])
        itemsList.append("`Qty: " + str(quantity) + "\tPrice: " + str(price) + "\tName: " + str(itemName) + "`")

editMessage = "> ### " + world + "\n"

for x in itemsList:
    editMessage += x + "\n"