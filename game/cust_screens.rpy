
init python:
    from inventory_objs import Inventory, Item, AddItem
    global_inventory = Inventory([])
    item_1 = Item("item_1")
    item_2 = Item("item_2")
    item_3 = Item("item_3")
    item_4 = Item("item_4")

screen choose_item:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 20
        imagebutton:
            background Frame("gui/frame.png")
            auto "gui/button/choice_%s_background.png"
            #text "Item 1"
            action [ToggleScreen("choose_item"), ToggleScreen("inventory_button"), Function(AddItem(Item("item_1"), global_inventory))]
        imagebutton:
            background Frame("gui/frame.png")
            auto "gui/button/choice_%s_background.png"
            #text "Item 2"
            action [ToggleScreen("choose_item"), ToggleScreen("inventory_button"), Function(AddItem(Item("item_2"), global_inventory))]
        imagebutton:
            background Frame("gui/frame.png")
            auto "gui/button/choice_%s_background.png"
            #text "Item 1"
            action [ToggleScreen("choose_item"),ToggleScreen("inventory_button"), Function(AddItem(Item("item_3"), global_inventory))]
        imagebutton:
            background Frame("gui/frame.png")
            auto "gui/button/choice_%s_background.png"
            #text "Item 1"
            action [ToggleScreen("choose_item"), ToggleScreen("inventory_button"), Function(AddItem(Item("item_4"), global_inventory))]


screen inventory_button():
    imagebutton:
        xalign 0.5
        yalign 0.5
        background Frame("gui/frame.png")
        auto "gui/button/choice_%s_background.png"
        #text "Inventory"
        action [ToggleScreen("inventory_button"), ToggleScreen("choose_item")]