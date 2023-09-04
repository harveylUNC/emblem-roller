#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


# In[1]:


import pandas as pd

champions = [
    {
        "name": "Cassiopeia",
        "cost": 1,
        "traits": ["Noxus", "Shurima", "Invoker"]
    },
    {
        "name": "Chogath",
        "cost": 1,
        "traits": ["Void", "Bruiser"]
    },
    {
        "name": "Irelia",
        "cost": 1,
        "traits": ["Ionia", "Challenger"]
    },
    {
        "name": "Jhin",
        "cost": 1,
        "traits": ["Ionia", "Deadeye"]
    },
    {
        "name": "Kayle",
        "cost": 1,
        "traits": ["Demacia", "Slayer"]
    },
    {
        "name": "Malzahar",
        "cost": 1,
        "traits": ["Void", "Sorcerer"]
    },
    {
        "name": "Maokai",
        "cost": 1,
        "traits": ["Shadow Isles", "Bastion"]
    },
    {
        "name": "Orianna",
        "cost": 1,
        "traits": ["Piltover", "Sorcerer"]
    },
    {
        "name": "Poppy",
        "cost": 1,
        "traits": ["Demacia", "Yordle", "Bastion"]
    },
    {
        "name": "Renekton",
        "cost": 1,
        "traits": ["Shurima", "Bruiser"]
    },
    {
        "name": "Samira",
        "cost": 1,
        "traits": ["Noxus", "Challenger"]
    },
    {
        "name": "Tristana",
        "cost": 1,
        "traits": ["Yordle", "Gunner"]
    },
    {
        "name": "Viego",
        "cost": 1,
        "traits": ["Shadow Isles", "Rogue"]
    },
    {
        "name": "Ashe",
        "cost": 2,
        "traits": ["Freljord", "Deadeye"]
    },
    {
        "name": "Galio",
        "cost": 2,
        "traits": ["Demacia", "Invoker"]
    },
    {
        "name": "Jinx",
        "cost": 2,
        "traits": ["Zaun", "Gunner"]
    },
    {
        "name": "Kassadin",
        "cost": 2,
        "traits": ["Void", "Bastion"]
    },
    {
        "name": "Kled",
        "cost": 2,
        "traits": ["Yordle", "Slayer", "Noxus"]
    },
    {
        "name": "Sett",
        "cost": 2,
        "traits": ["Ionia", "Juggernaut"]
    },
    {
        "name": "Soraka",
        "cost": 2,
        "traits": ["Targon", "Invoker"]
    },
    {
        "name": "Swain",
        "cost": 2,
        "traits": ["Noxus", "Strategist", "Sorcerer"]
    },
    {
        "name": "Taliyah",
        "cost": 2,
        "traits": ["Shurima", "Multicaster"]
    },
    {
        "name": "Teemo",
        "cost": 2,
        "traits": ["Yordle", "Multicaster", "Strategist"]
    },
    {
        "name": "Vi",
        "cost": 2,
        "traits": ["Piltover", "Bruiser"]
    },
    {
        "name": "Warwick",
        "cost": 2,
        "traits": ["Zaun", "Challenger"]
    },
    {
        "name": "Zed",
        "cost": 2,
        "traits": ["Ionia", "Rogue", "Slayer"]
    },
    {
        "name": "Akshan",
        "cost": 3,
        "traits": ["Shurima", "Deadeye"]
    },
    {
        "name": "Darius",
        "cost": 3,
        "traits": ["Noxus", "Juggernaut"]
    },
    {
        "name": "Ekko",
        "cost": 3,
        "traits": ["Piltover", "Zaun", "Rogue"]
    },
    {
        "name": "Garen",
        "cost": 3,
        "traits": ["Demacia", "Juggernaut"]
    },
    {
        "name": "Jayce",
        "cost": 3,
        "traits": ["Piltover", "Gunner"]
    },
    {
        "name": "Karma",
        "cost": 3,
        "traits": ["Ionia", "Invoker"]
    },
    {
        "name": "Katarina",
        "cost": 3,
        "traits": ["Noxus", "Rogue"]
    },
    {
        "name": "Lissandra",
        "cost": 3,
        "traits": ["Freljord", "Invoker"]
    },
    {
        "name": "RekSai",
        "cost": 3,
        "traits": ["Void", "Bruiser"]
    },
    {
        "name": "Sona",
        "cost": 3,
        "traits": ["Demacia", "Multicaster"]
    },
    {
        "name": "Taric",
        "cost": 3,
        "traits": ["Targon", "Bastion", "Sorcerer"]
    },
    {
        "name": "Velkoz",
        "cost": 3,
        "traits": ["Void", "Sorcerer", "Multicaster"]
    },
    {
        "name": "Aphelios",
        "cost": 4,
        "traits": ["Targon", "Deadeye"]
    },
    {
        "name": "Azir",
        "cost": 4,
        "traits": ["Shurima", "Strategist"]
    },
    {
        "name": "Gwen",
        "cost": 4,
        "traits": ["Shadow Isles", "Slayer"]
    },
    {
        "name": "Jarvan IV",
        "cost": 4,
        "traits": ["Demacia", "Strategist"]
    },
    {
        "name": "Kaisa",
        "cost": 4,
        "traits": ["Void", "Challenger"]
    },
    {
        "name": "Lux",
        "cost": 4,
        "traits": ["Demacia", "Sorcerer"]
    },
    {
        "name": "Nasus",
        "cost": 4,
        "traits": ["Shurima", "Juggernaut"]
    },
    {
        "name": "Sejuani",
        "cost": 4,
        "traits": ["Freljord","Bruiser"]
    },
    {
        "name": "Shen",
        "cost": 4,
        "traits": ["Ionia","Bastion","Invoker"]
    },
    {
        "name": "Urgot",
        "cost": 4,
        "traits": ["Zaun","Deadeye"]
    },
    {
        "name": "Yasuo",
        "cost": 4,
        "traits": ["Ionia","Challenger"]
    },
    {
        "name": "Zeri",
        "cost": 4,
        "traits": ["Zaun","Gunner"]
    },
    {
        "name": "Aatrox",
        "cost": 5,
        "traits": ["Darkin","Slayer","Juggernaut"]
    },
    {
        "name": "Ahri",
        "cost": 5,
        "traits": ["Ionia","Sorcerer"]
    },
    {
        "name": "Belveth",
        "cost": 5,
        "traits": ["Empress","Void"]
    },
    {
        "name": "Heimerdinger",
        "cost": 5,
        "traits": ["Yordle","Piltover","Technogenius"]
    },
    {
        "name": "KSante",
        "cost": 5,
        "traits": ["Bastion","Shurima"]
    },
    {
        "name": "Ryze",
        "cost": 5,
        "traits": ["Wanderer","Invoker"]
    },
    {
        "name": "Senna",
        "cost": 5,
        "traits": ["Shadow Isles","Gunner","Redeemer"]
    },
    {
        "name": "Sion",
        "cost": 5,
        "traits": ["Noxus","Bruiser"]
    }
]


# In[3]:


champions = pd.DataFrame(champions)


# # Emblems

# In[4]:


emblems = [
    "Bastion",
    "Bruiser",
    "Challenger",
    "Deadeye",
    "Demacia",
    "Freljord",
    "Gunner",
    "Ionia",
    "Invoker",
    "Juggernaut",
    "Noxus",
    "Piltover",
    "Rogue",
    "Shadow Isles",
    "Shurima",
    "Slayer",
    "Sorcerer",
    "Strategist",
    "Targon",
    "Void",
    "Zaun"
]


# # Implement Algo

# In[5]:


def optimal_units(units, board_capacity, desired_emblems, available_traits):
    df = pd.DataFrame(units)

    # find all possible combinations of units up to board_capacity
    unit_combinations = []
    for r in range(1, min(board_capacity, len(df)) + 1):
        combinations_obj = itertools.combinations(df['name'], r)
        unit_combinations += list(combinations_obj)

    # find combination with the highest chance of getting one of the desired emblems
    max_chance = -np.inf
    best_combination = None
    for combination in unit_combinations:
        traits = df[df['name'].isin(combination)]['traits'].sum()

        unique_traits = len(set(traits))

        if unique_traits >= 6:

            #probability based on number of tailored emblems
            exponent = 1
            if unique_traits >= 8 and unique_traits < 10:
                exponent = 2
            elif unique_traits >= 10 and unique_traits < 12:
                exponent = 3
            elif unique_traits >= 12:
                exponent = 4
            
            # count unique available vs desired traits
            available_unique_traits = len(set([t for t in traits if t in available_traits]))
            count_desired_traits = len([t for t in set(traits) if t in desired_emblems])

            # calculate chance of getting one of the desired emblems
            if available_unique_traits != 0:
                chance = 1-(1- count_desired_traits / available_unique_traits)**exponent
                if chance > max_chance and count_desired_traits > 0:
                    max_chance = chance
                    best_combination = combination
    return best_combination, max_chance


# # Create Game

# ## Interfacing and Notifications

# In[6]:


def create_level_interface():
    prompt_label.show()
    prompt_label.set_text('Select Board Size')
    for i in range(3, 12):
        button_rect = pygame.Rect((350, 60 * (i - 2)), (100, 50))
        number_buttons.append(pygame_gui.elements.UIButton(relative_rect=button_rect,
                                                           text=str(i),
                                                           manager=manager))


# In[7]:


def create_warning_popup(type):
    popup_dialog = pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect((200, 200), (400, 200)),
                                                           manager=manager,
                                                           window_title="Warning",
                                                           action_long_desc=f"You have selected too many {type}!",
                                                           action_short_name="OK",
                                                           blocking=True)
    popup_dialog.dialog_text = "OK"


# In[8]:


def create_interface():
    max_visible_checkboxes = 100
    checkbox_height = 20
    for i in range(1, 6):
        height_counter = 0
        for j, champion_name in enumerate(champions_names[scrolling_offset:scrolling_offset + max_visible_checkboxes]):
            if champions.loc[champions['name'] == champion_name, 'cost'].values[0] == i:
                height_counter += 1
                checkbox_rect = pygame.Rect((100 + 110 * (i - 1), 30 + height_counter * checkbox_height), (110, checkbox_height))
                checkbox = pygame_gui.elements.UIButton(relative_rect=checkbox_rect,
                                                        text=champion_name,
                                                        manager=manager)
                champion_checkboxes.append(checkbox)

    # create emblem checkboxes
    emblems_names = pd.Series(emblems)
    emblem_length_counter = 0
    emblem_height_counter = 0
    for emblem_name in emblems_names:
        if emblem_height_counter == 4:
            emblem_length_counter += 1
            emblem_height_counter = 0
        emblem_checkbox_rect = pygame.Rect((100 + 110*emblem_length_counter, 390 + emblem_height_counter * checkbox_height), (110, checkbox_height))
        emblem_checkbox = pygame_gui.elements.UIButton(relative_rect=emblem_checkbox_rect,
                                                      text=emblem_name,
                                                      manager=manager)
        emblem_checkboxes.append(emblem_checkbox)
        emblem_height_counter += 1

    # Create clear, go checkboxes
    clearchamp_checkbox_rect = pygame.Rect((100, 520), (150, checkbox_height))
    clearchamp_checkbox = pygame_gui.elements.UIButton(relative_rect=clearchamp_checkbox_rect,
                                                      text='Clear Champs',
                                                      manager=manager)
    tools_checkboxes.append(clearchamp_checkbox)
    
    clearemblem_checkbox_rect = pygame.Rect((250, 520), (150, checkbox_height))
    clearemblem_checkbox = pygame_gui.elements.UIButton(relative_rect=clearemblem_checkbox_rect,
                                                      text='Clear Emblems',
                                                      manager=manager)
    tools_checkboxes.append(clearemblem_checkbox)
    
    start_checkbox_rect = pygame.Rect((400, 520), (150, checkbox_height))
    start_checkbox = pygame_gui.elements.UIButton(relative_rect=start_checkbox_rect,
                                                      text='START',
                                                      manager=manager)
    tools_checkboxes.append(start_checkbox)
    level_checkbox_rect = pygame.Rect((550, 520), (150, checkbox_height))
    level_checkbox = pygame_gui.elements.UIButton(relative_rect=level_checkbox_rect,
                                                      text='Change Level',
                                                      manager=manager)
    tools_checkboxes.append(level_checkbox)
 
    


# ## Running Game

# In[ ]:


import pygame
import pygame_gui
import pandas as pd
import itertools
import numpy as np

pygame.init()

size = (800, 600)
window_surface = pygame.display.set_mode(size)
    
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()
is_running = True

board_size = None  
selected_champions = [] 
selected_emblems = []  

scrolling_offset = 0  
scroll_speed = 20  

manager = pygame_gui.UIManager(size, "theme.json")

# text label for entering board size
prompt_label_rect = pygame.Rect((300, 10, 200, 50))
prompt_label = pygame_gui.elements.UILabel(relative_rect=prompt_label_rect,
                                           text='Enter Board Size',
                                           manager=manager)

# text label for displaying selected board size
display_label_rect = pygame.Rect((300, 10, 200, 50))
display_label = pygame_gui.elements.UILabel(relative_rect=display_label_rect,
                                            text='',
                                            manager=manager)

# text label for displaying selected board/bench units
units_label_rect = pygame.Rect((0, 310, 700, 70))
units_label = pygame_gui.elements.UITextBox(relative_rect=units_label_rect,
                                          html_text='',
                                          manager=manager)

# text label for displaying selected emblems
emblems_label_rect = pygame.Rect((0, 480, 700, 40))
emblems_label = pygame_gui.elements.UITextBox(relative_rect=emblems_label_rect,
                                            html_text='',
                                            manager=manager)

# text label for displaying selected emblems
solution_label_rect = pygame.Rect((0, 540, 700, 40))
solution_label = pygame_gui.elements.UITextBox(relative_rect=solution_label_rect,
                                            html_text='',
                                            manager=manager)

# create champion checkboxes
champions_names = champions['name']

champion_checkboxes = []
emblem_checkboxes = []
tools_checkboxes = []
number_buttons = []

units_label.hide()
emblems_label.hide()
solution_label.hide()
board_size;
while is_running:
    if board_size is None:
        create_level_interface();
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element in number_buttons:
                    prompt_label.hide()
                    display_label.show()
                    for i in range(len(number_buttons)):
                        if event.ui_element == number_buttons[i]:
                            board_size = int(event.ui_element.text)
                            display_label.set_text('Board Size: ' + str(board_size))
                            # Hide buttons after selection
                            for button in number_buttons:
                                button.hide()
                            prompt_label.hide()
                    create_interface()
  
                            
            # Handle checkbox clicks
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element in champion_checkboxes:
                    solution_label.hide()
                    button_text = event.ui_element.text
                    if button_text in selected_champions:
                        selected_champions.remove(button_text)
                    else:
                        selected_champions.append(button_text)
                    units_label.set_text(', '.join(selected_champions))  # Update the units label text
                    units_label.show()
                    
                elif event.ui_element in emblem_checkboxes:
                    solution_label.hide()
                    button_text = event.ui_element.text
                    if button_text in selected_emblems:
                        selected_emblems.remove(button_text)
                    else:
                        selected_emblems.append(button_text)
                    emblems_label.show()
                    print(selected_emblems)
                    emblems_label.set_text(', '.join(selected_emblems))  # Update the emblems label text
                elif event.ui_element in tools_checkboxes:
                    button_text = event.ui_element.text
                    if button_text == 'Clear Champs':
                        selected_champions.clear()
                        units_label.set_text(', '.join(selected_champions))  # Update the units label text
                        units_label.hide()
                    elif button_text == 'Clear Emblems':
                        selected_emblems.clear()
                        emblems_label.set_text(', '.join(selected_emblems))  # Update the emblems label text
                        emblems_label.hide()
                    elif button_text == 'START':
                        champs_list = pd.DataFrame(champions)
                        champs_list = champs_list[champs_list['name'].isin(selected_champions)].to_dict(orient='records')
                        solution, chance = optimal_units(champs_list,board_size,selected_emblems,emblems)
                        print(solution)
                        if solution is None:
                            solution_label.set_text('No Solution')
                        elif len(solution) == 1:
                            solution_label.set_text(solution[0])  # Update the solution label text
                        else:
                            solution_label.set_text(', '.join(solution)+', Chance:' + str(chance))  # Update the solution label text
                        solution_label.show()
                    elif button_text == 'Change Level':
                        selected_champions = []
                        selected_emblems = []
                        emblems_label.hide()
                        units_label.hide()
                        solution_label.hide()
                        display_label.hide()
                        for checkbox in (champion_checkboxes + emblem_checkboxes + tools_checkboxes):
                            checkbox.hide()
                        print(board_size)
                        board_size = None
                        print(board_size)
                        create_level_interface()
                            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # scroll up
                scrolling_offset = max(scrolling_offset - 1, 0)
            elif event.button ==0:  # scroll down
                scrolling_offset = min(scrolling_offset + 1, len(champions_names) - max_visible_checkboxes)
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
    
pygame.quit() 


# In[ ]:




