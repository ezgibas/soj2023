# main script - this is where all the variables are defined
# and the rough outline is set
# to edit details about each part, go to the corresponding script


# --- Python Initialize ---
# import custom python objects for inventory mechanic
init python:
    from inventory_objs import Inventory, Item
    global_inventory = Inventory([])
    item_limit = 2

# --- Characters ---
define m = Character("Magnolia")

# --- Images ---
image morning house bg = "../images/morning_house_bg.png"
image crow land = "../images/crow_land.png"
image ink seep = "../images/ink_seep.png"
image list1 = "../images/list.png"
image messy desk = "../images/messy_desk.png"
image ritual calendar = "../images/ritual_calendar.png"
image ritual message = "../images/ritual_message.png"
image window_view = "../images/window_view.png"
#image crowded cabinet = "../images/crowded_cabinet.png"

# --- Items ---
# swamp items
define mud = Item("mud")
define water = Item("water")
define algae = Item("algae")

# tree items
define wasps = Item("wasps")
define caterpillars = Item("caterpillars")
define lichens = Item("lichens")
define leaves = Item("leaves")

# garden items
# rock items
define worms = Item("worms")
define weevils = Item("weevils")
define grubs = Item("grubs")
define moss = Item("moss")

# flowerbed items
define flowers = Item("flowers")
define clovers = Item("clovers")
define bumblebees = Item("bumblebees")

# --- GAME SCRIPT ---

label start:
    python:
        global_inventory.reset()
        items_collected = 0
    #call exposition
    #call inciting_incident
    call rising_action

    return

