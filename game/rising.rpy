label rising_action:
    python:
        items_collected = 0
        item_limit = 2
    "You have to prepare immediately. The ritual will be performed at sundown, the precise time you have predicted the emergence of cicadas. "
    "It is smartest to search outside first, while you still have sunlight overhead."
    show window_view

    "The grass is soft beneath your feet as you step out. The cicadas are beneath you. You can only hope for their cooperation with you tonight…"

    call collection_menu

    label collection_menu_end:
        "You have everything you remember needing from the outside… you think…"
        "Time to head inside and collect the rest. The sun is overhead, and you are wary of the passage of time. "

    return


menu collection_menu:
    "Head to the swamp" if items_collected < item_limit:
        call screen swamp
        return

    "Look up to the trees" if items_collected < item_limit:
        call screen trees
        return

    "Wander your garden" if items_collected < item_limit:
        jump garden_menu
    
    "Done Collecting" if items_collected >= item_limit:
        return



menu garden_menu:
    "Turn a rock":
        call screen rock
        return
    "Check the flowerbed":
        call screen flowerbed
        return
    "Go Back":
        return