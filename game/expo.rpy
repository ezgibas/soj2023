# main script of the exposition
label exposition:
    python:
        show_mirror = True
        show_desk = True
        show_cabinet = True
    show morning house bg
    m "Ugh..."
    m "Where is my wand..?"
    "You get up from your bed, your joints creaking as you slowly stand. Your hands are solidly on your knees, and you hunch over in search of your wand. "
    jump get_up_menu

    label get_up_menu_end:
        "You are coming to terms with your sudden bouts of forgetfulness, staggering to the window to look outside."
        "You suppose maybe these things simply come with age, and thusly you will accept them with open arms. On the other hand, you are not nearly as accepting of your increased clumsiness…"
        "There, by the door! How did you miss it?"
        "You lean your weight on the wand once you are reunited with it. It supports you while leaning out the window."
        "The breeze hits your face - it is very warm today, just as you had divined. The power of truth that lies in the swamp mud has never misled you."
        "The deep comfort you are filled with as you gaze outside is quickly interrupted by a crow flying into view."
        "Your heart sinks, and you grip the wand harder. You feel the harsh edges of the stones embedded in the old wooden staff. It grounds you. "
    
    return
    

# menu for getting up
menu get_up_menu:
    "Go to the mirror" if show_mirror:
        $ show_mirror = False
        show mirror reflection
        "You are weathered by age, but your eyes show you have smiled a lot in this life. The lines that have been carved into your features delineate your experience.  You consider taming your morning hair for a few seconds but quickly abandon the thought."
        jump mirror_menu

    "Go to the desk" if show_desk:
        $ show_desk = False
        show messy desk
        m "I usually leave it right here, where did I put it?"
        jump desk_menu

    "Go to the cabinet" if show_cabinet:
        $ show_cabinet = False
        show crowded cabinet


# menu for mirror
menu mirror_menu:
    "Look at photograph":
        "Flip: Almira, Tabitha, Patience, and I. 1870." # TODO FLIP
        jump mirror_menu

    "Walk Away":
        jump menu_controller

# menu for desk
menu desk_menu:
    "Look at framed photographs":
        "Flip: Everyone together again! 1888. "
        "Flip 2: Drawing by Patience and Magnolia. 1840."
        jump desk_menu

    "Read letter":
        "Letter: Regarding Almira (about her absence) "
        jump desk_menu

    "Walk away":
        jump menu_controller

# menu for cabinet
menu cabinet_menu:
    "Look at the ingredients":
        "You’ve been stocking up for a while. With the ritual today, you have the most important stuff pulled up to the front since you are so forgetful. "
        jump cabinet_menu

    "Look at potions":
        "These potions have been warding off evil spirits well enough thus far. Some are labeled: Almira, Tabitha, Patience, and Magnolia. The Almira one has a crack in it. You squint at it. "
        jump cabinet_menu

    "Walk away":
        jump menu_controller

# menu controller
label menu_controller:
    if  (not show_mirror) and (not show_desk) and (not show_cabinet):
        jump get_up_menu_end
    else:
        jump get_up_menu