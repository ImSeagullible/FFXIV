import tkinter as tk
import json
from urllib.request import Request, urlopen

def validate_input(input):
    # Check if the input is an integer
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

root = tk.Tk()
root.title("Materia Labels")
root.geometry("1275x500")

# Register the validation command
vcmd = root.register(validate_input)

# Dictionary of sections
sections = {
    "Melee": ["Heavens' Eye", "Savage Aim", "Savage Might"],
    "Caster": ["Quickarm", "Quicktongue"],
    "Support": ["Piety", "Battledance"],
    "Crafter": ["Craftsman's Competence", "Craftsman's Cunning", "Craftsman's Command"],
    "Gatherer": ["Gatherer's Guerdon", "Gatherer's Guile", "Gatherer's Grasp"]
}

itemIds = {
    "Heavens' Eye IX": 33918,
    "Heavens' Eye X": 33931,
    "Savage Aim IX": 33919,
    "Savage Aim X": 33932,
    "Savage Might IX": 33920,
    "Savage Might X": 33933,
    "Quickarm IX": 33928,
    "Quickarm X": 33941,
    "Quicktongue IX": 33929,
    "Quicktongue X": 33942,
    "Piety IX": 33917,
    "Piety X": 33930,
    "Battledance IX": 33921,
    "Battledance X": 33934,
    "Craftsman's Competence IX": 33925,
    "Craftsman's Competence X": 33938,
    "Craftsman's Cunning IX": 33926,
    "Craftsman's Cunning X": 33939,
    "Craftsman's Command IX": 33927,
    "Craftsman's Command X": 33940,
    "Gatherer's Guerdon IX": 33922,
    "Gatherer's Guerdon X": 33935,
    "Gatherer's Guile IX": 33923,
    "Gatherer's Guile X": 33936,
    "Gatherer's Grasp IX": 33924,
    "Gatherer's Grasp X": 33937
}

# Define the grid layout
grid_layout = [
    ["Melee", "Caster", "Support"],
    ["Crafter", "Gatherer"]
]

# Set a minimum row height in pixels
min_row_height = 200

# Create the sections, labels, and entries
for row in range(len(grid_layout)):
    root.grid_rowconfigure(row, minsize=min_row_height)
    for column in range(len(grid_layout[row])):
        section = grid_layout[row][column]
        items = sections[section]

        # Create a new frame for the section
        section_frame = tk.Frame(root, bd=5, relief="groove")
        section_frame.grid(row=row, column=column, sticky='nsew')

        # Create the section label
        section_label = tk.Label(section_frame, text=section)
        section_label.pack(anchor='nw')

        # Create the labels and entries for each item
        for item in items:
            # Create a new frame for the item
            item_frame = tk.Frame(section_frame)
            item_frame.pack(anchor='nw')

            # Create the item label
            item_label = tk.Label(item_frame, text=item)
            item_label.pack(anchor='nw')

            # Create the "IX" label and entry
            ix_label = tk.Label(item_frame, text="IX")
            ix_label.pack(side='left')
            ix_entry = tk.Entry(item_frame, validate='key', validatecommand=(vcmd, '%P'))  # Add validation
            ix_entry.pack(side='left')

            # Create the "X" label and entry
            x_label = tk.Label(item_frame, text="X")
            x_label.pack(side='left')
            x_entry = tk.Entry(item_frame, validate='key', validatecommand=(vcmd, '%P'))  # Add validation
            x_entry.pack(side='left')

# Create a Text widget on the right side of the window
text_widget = tk.Text(root, width=50)
text_widget.grid(row=0, column=len(grid_layout[0]), rowspan=len(grid_layout), sticky='nsew')

def getJsonObj(world, itemID):
    link = "https://universalis.app/api/" + str(world) + "/" + str(itemID)
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    jsonListOfItems = urlopen(req).read().decode("utf-8")
    return jsonListOfItems

def getAllAuctions(world, itemID):
    jsonList = getJsonObj(world, itemID)
    jsonObject = json.loads(jsonList)
    numOfPosts = len(jsonObject["listings"])
    listOfImportantInfo = []
    for x in range(numOfPosts):
        retainerName = str(jsonObject["listings"][x]["retainerName"])
        quantity = str(jsonObject["listings"][x]["quantity"])
        pricePerUnit = str(jsonObject["listings"][x]["pricePerUnit"])
        listOfImportantInfo.append([retainerName, quantity, pricePerUnit])
    return listOfImportantInfo

def getLowestPrice(world, itemid):
    itemList = getAllAuctions(world, itemid)
    min = 99999999999999
    for x in itemList:
        if int(x[2]) < int(min):
            min = x[2]
    return min

def populate_from_api():
    counter = 0
    # Iterate over all the children of the root window
    for child in root.winfo_children():
        # Check if the child is a Frame (which contains the Entry widgets)
        if isinstance(child, tk.Frame):
            # Iterate over all the children of the Frame
            for grandchild in child.winfo_children():
                # Check if the grandchild is a Frame (which contains the Entry widgets)
                if isinstance(grandchild, tk.Frame):
                    # Iterate over all the children of the grandchild Frame
                    entries = list(filter(lambda x: isinstance(x, tk.Entry), grandchild.winfo_children()))
                    if entries:
                        lbltxt = grandchild.winfo_children()[0].cget("text")
                        ixtxt = lbltxt + " IX"

                        low = getLowestPrice('Ultros', int(itemIds.get(ixtxt)))
                        # Set the value of the IX Entry
                        entries[0].delete(0, 'end')
                        entries[0].insert(0, str(low))

                        xtxt = lbltxt + " X"
                        low = getLowestPrice('Ultros', int(itemIds.get(xtxt)))
                        # Set the value of the X Entry
                        entries[1].delete(0, 'end')
                        entries[1].insert(0, str(low))


# Create the "Import Data from Universalis" button
import_button = tk.Button(root, text="Import Data from Universalis", width=40, height=5, pady=5, command=populate_from_api)
import_button.grid(row=len(grid_layout), column=0, sticky='sw')

def calculate_average():
    text_widget.delete('1.0', 'end')
    # Initialize the sum for IX and X
    sum_ix = 0
    sum_x = 0
    # Initialize the count
    count = 0
    # Initialize the minimum value to a large number
    min_value_ix = float('inf')
    min_value_x = float('inf')
    # Initialize the labels for the items with the lowest value
    min_label_ix = ""
    min_label_x = ""

    # Iterate over all the children of the root window
    for child in root.winfo_children():
        # Check if the child is a Frame (which contains the Entry widgets)
        if isinstance(child, tk.Frame):
            # Iterate over all the children of the Frame
            for grandchild in child.winfo_children():
                # Check if the grandchild is a Frame (which contains the Entry widgets)
                if isinstance(grandchild, tk.Frame):
                    # Get the item label
                    item_label = grandchild.winfo_children()[0].cget("text")
                    # Iterate over all the children of the grandchild Frame
                    entries = list(filter(lambda x: isinstance(x, tk.Entry), grandchild.winfo_children()))
                    if entries:
                        # Get the value of the IX Entry
                        value_ix = entries[0].get()
                        # Get the value of the X Entry
                        value_x = entries[1].get()
                        # Check if the value is not an empty string
                        if value_ix:
                            # Convert the value to an integer
                            value_ix = int(value_ix)
                            # Add the value to the sum
                            sum_ix += value_ix
                            # Update the minimum value and label
                            if value_ix < min_value_ix:
                                min_value_ix = value_ix
                                min_label_ix = item_label
                        if value_x:
                            # Convert the value to an integer
                            value_x = int(value_x)
                            # Add the value to the sum
                            sum_x += value_x
                            # Update the minimum value and label
                            if value_x < min_value_x:
                                min_value_x = value_x
                                min_label_x = item_label
                        # Increment the count
                        count += 1

    # Calculate the average
    average_ix = sum_ix / 12
    average_x = sum_x / 12
    # Calculate the lowest cost
    lowest_cost_ix = min_value_ix * 5
    lowest_cost_x = min_value_x * 5
    # Insert the results into the Text widget
    text_widget.insert('end', f"Average value for IX is: {average_ix}\n")
    text_widget.insert('end', f"The Lowest Cost for IX is: {lowest_cost_ix} \n(from {min_label_ix})\n\n\n")
    text_widget.insert('end', f"Average value for X is: {average_x}\n")
    text_widget.insert('end', f"The Lowest Cost for X is: {lowest_cost_x} \n(from {min_label_x})\n")


# Create the "Apply Values" button
apply_button = tk.Button(root, text="Apply Values", width=40, height=5, pady=5, command=calculate_average)
apply_button.grid(row=len(grid_layout), column=len(grid_layout[0]), sticky='se')

root.mainloop()