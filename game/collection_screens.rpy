# custom buttons for collection mechanic

define img = "../images/button/mud_%s.png" 

    

screen swamp:
    grid 1 2:
        xalign 0.5
        yalign 0.5
        spacing 70
        grid 3 1:
            spacing 40
            vbox:
                imagebutton:
                    auto img # "images/button/mud_%s.png"
                    action [Call("collect_item_confirm", "mud", "swamp")]
                label "mud"
            vbox:
                imagebutton:
                    auto img # "images/button/water_%s.png"
                    action [Call("collect_item_confirm", "water", "swamp")]
                label "water"
            vbox:
                imagebutton:
                    auto img # "images/button/algae_%s.png"
                    action [Call("collect_item_confirm", "algae", "swamp")]
                label "algae"
        frame:
            textbutton "Back":
                action [Jump("collection_menu")]

screen trees:
    grid 1 2:
        xalign 0.5
        yalign 0.5
        spacing 70
        grid 2 2:
            spacing 30
            vbox:
                imagebutton:
                    auto img # "images/button/wasps_%s.png"
                    action [Call("collect_item_confirm", "wasps", "trees")]
                label "wasps"
            vbox:
                imagebutton:
                    auto img # "images/button/caterpillars_%s.png"
                    action [Call("collect_item_confirm", "caterpillars", "trees")]
                label "caterpillars"
            vbox:
                imagebutton:
                    auto img # "images/button/lichens_%s.png"
                    action [Call("collect_item_confirm", "lichens", "trees")]
                label "lichens"
            vbox:
                imagebutton:
                    auto img # "images/button/leaves_%s.png"
                    action [Call("collect_item_confirm", "leaves", "trees")]
                label "leaves"
        frame:
            textbutton "Back":
                action [Jump("collection_menu")]

screen rock:
    grid 1 2:
        xalign 0.5
        yalign 0.5
        spacing 70
        grid 2 2:
            spacing 30
            vbox:
                imagebutton:
                    auto img # "images/button/worms_%s.png"
                    action [Call("collect_item_confirm", "worms", "rock")]
                label "worms"
            vbox:
                imagebutton:
                    auto img # "images/button/weevils_%s.png"
                    action [Call("collect_item_confirm", "weevils", "rock")]
                label "weevils"
            vbox:
                imagebutton:
                    auto img # "images/button/grubs_%s.png"
                    action [Call("collect_item_confirm", "grubs", "rock")]
                label "grubs"
            vbox:
                imagebutton:
                    auto img # "images/button/moss_%s.png"
                    action [Call("collect_item_confirm", "moss", "rock")]
                label "moss"
        frame:
            textbutton "Back":
                action [Jump("collection_menu")]

screen flowerbed:
    grid 1 2:
        xalign 0.5
        yalign 0.5
        spacing 50
        grid 1 3:
            spacing 20
            vbox:
                imagebutton:
                    auto img # "images/button/flowers_%s.png"
                    action [Call("collect_item_confirm", "flowers", "flowerbed")]
                label "flowers"
            vbox:
                imagebutton:
                    auto img # "images/button/clovers_%s.png"
                    action [Call("collect_item_confirm", "clovers", "flowerbed")]
                label "clovers"
            vbox:
                imagebutton:
                    auto img # "images/button/bumblebees_%s.png"
                    action [Call("collect_item_confirm", "bumblebees", "flowerbed")]
                label "bumblebees"
        frame:
            textbutton "Back":
                action [Jump("collection_menu")]


# ask user if they want to collect the selected item
label collect_item_confirm(item_name, original_screen):
    if global_inventory.hasitem(Item(item_name)):
        "You already have [item_name]!"
        call screen expression original_screen  

    else:
        "Collect [item_name]?"
        menu:
            "Yes": 
                $ items_collected += 1
                $ global_inventory.additem(Item(item_name))
                "You collected [item_name]!"
                call collection_menu_control(original_screen)
                return

            "No":
                call collection_menu_control(original_screen)  
                return
                
# if user has collected all items, return to narration
# otherwise, go back to the screen you came from
label collection_menu_control(original_screen):
    if items_collected >= item_limit:
        "Your pockets are full."
        return
    else:
        call screen expression original_screen