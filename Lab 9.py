
""" COMP-593
    Scripting Lab 9
    Norlon Sibug
    10312229
    nsibug@flemingcollege.ca

    # Citation for the video:
# Title: "Python GUI With Tkinter Tutorial | Make A Pokedex GUI Application With Tkinter"
# Creator: Coding Abs
# Date Published: January 19, 2021
# URL: https://www.youtube.com/watch?v=T_Ja8_R0Bio
# Note: This code uses the video for educational purposes only.
# This video was used as a resource for understanding Python programming basics.

""" 
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import pygame
from io import BytesIO
from poke_api import get_pokemon_info  # Ensure this function fetches data from PokéAPI

def play_music():
    pygame.mixer.init()  # Initialize the mixer
    pygame.mixer.music.load("pokemon_song.mp3")  # Load your music file
    pygame.mixer.music.set_volume(0.1)  # Set the volume to 10%
    pygame.mixer.music.play(-1)  # Play in a loop (-1 means infinite loop)

def increase_volume():
        current_volume = pygame.mixer.music.get_volume()
        if current_volume < 1.0:
            pygame.mixer.music.set_volume(max(current_volume + 0.1, 1.0))

def decrease_volume():
        current_volume = pygame.mixer.music.get_volume()
        if current_volume > 0.0:
            pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))


def puase_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def main():
    root = Tk()
    root.title("Pokémon Information")
    root.geometry("800x600")

    play_music()

    bg_img = Image.open('images.png')
    bg_img = bg_img.resize((800, 600))
    bg_img = ImageTk.PhotoImage(bg_img)
    bg_label = Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    bg_label.image = bg_img  # Keep a reference to avoid garbage collection

    btn_volume_up = ttk.Button(root, text="Volume Up", command=increase_volume)
    btn_volume_up.place(x=10, y=250)

    btn_volume_down = ttk.Button(root, text="Volume Down", command=decrease_volume)
    btn_volume_down.place(x=150, y=250)

    btn_pause = ttk.Button(root, text="Pause", command=puase_music)
    btn_pause.place(x=10, y=280)
    
    btn_unpause = ttk.Button(root, text="Unpause", command=unpause_music)
    btn_unpause.place(x=150, y=280)

    # User input frame
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
    lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1)

    def handle_btn_get_info():
        pokemon = ent_name.get().strip().lower()
        poke_info = get_pokemon_info(pokemon)

        if poke_info:
            # Update labels with Pokémon details
            lbl_height_val['text'] = str(poke_info['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'

            types = [t["type"]["name"] for t in poke_info["types"]]
            lbl_type_val["text"] = ", ".join(types)

            # Update stats
            bar_hp['value'] = poke_info['stats'][0]['base_stat']
            bar_attack['value'] = poke_info['stats'][1]['base_stat']
            bar_defense['value'] = poke_info['stats'][2]['base_stat']
            bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
            bar_special_defense['value'] = poke_info['stats'][4]['base_stat']
            bar_speed['value'] = poke_info['stats'][5]['base_stat']

            # Fetch and display Pokémon image
            sprite_url = poke_info['sprites']['front_default']
            if sprite_url:
                response = requests.get(sprite_url)
                img_data = Image.open(BytesIO(response.content))
                img_data = img_data.resize((150, 150))  # Resize to fit UI
                photo = ImageTk.PhotoImage(img_data)
                lbl_image.config(image=photo)
                lbl_image.image = photo  # Keep a reference to avoid garbage collection
        else:
            messagebox.showerror(message=f"I can't find this Pokémon: {pokemon}. Please try again.", title="Error")

    btn_get_info = ttk.Button(frm_input, text='Get Info', command=handle_btn_get_info)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10, sticky=W)

    # Info frame
    lblfrm_info = ttk.LabelFrame(root, text="Info")
    lblfrm_info.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

    lbl_height = ttk.Label(lblfrm_info, text="Height:")
    lbl_height.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)
    lbl_height_val = ttk.Label(lblfrm_info, width=20)
    lbl_height_val.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky=W)

    lbl_weight = ttk.Label(lblfrm_info, text="Weight:")
    lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=E)
    lbl_weight_val = ttk.Label(lblfrm_info)
    lbl_weight_val.grid(row=1, column=1, padx=(0, 10), pady=5, sticky=W)

    lbl_type = ttk.Label(lblfrm_info, text="Type(s):")
    lbl_type.grid(row=2, column=0, padx=(10, 5), pady=5, sticky=E)
    lbl_type_val = ttk.Label(lblfrm_info, width=20)
    lbl_type_val.grid(row=2, column=1, padx=(0, 10), pady=5, sticky=W)

    # Stats frame
    lblfrm_stats = ttk.LabelFrame(root, text="Stats")
    lblfrm_stats.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky=N)

    lbl_hp = ttk.Label(lblfrm_stats, text="HP:")
    lbl_hp.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=E)
    bar_hp = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_hp.grid(row=0, column=1, padx=(0, 10), pady=(10, 5))

    lbl_attack = ttk.Label(lblfrm_stats, text="Attack:")
    lbl_attack.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_attack.grid(row=1, column=1, padx=(0, 10), pady=5)

    lbl_defense = ttk.Label(lblfrm_stats, text="Defense:")
    lbl_defense.grid(row=2, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_defense.grid(row=2, column=1, padx=(0, 10), pady=5)

    lbl_special_attack = ttk.Label(lblfrm_stats, text="Special Attack:")
    lbl_special_attack.grid(row=3, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_special_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_special_attack.grid(row=3, column=1, padx=(0, 10), pady=5)

    lbl_special_defense = ttk.Label(lblfrm_stats, text="Special Defense:")
    lbl_special_defense.grid(row=4, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_special_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_special_defense.grid(row=4, column=1, padx=(0, 10), pady=5)

    lbl_speed = ttk.Label(lblfrm_stats, text="Speed:")
    lbl_speed.grid(row=5, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_speed = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_speed.grid(row=5, column=1, padx=(0, 10), pady=5)

    # Pokémon Image
    lbl_image = Label(root)
    lbl_image.grid(row=10, column=0,  padx=40, pady=(5, 10), sticky=W)

    img = Image.open('pokemon1.png')
    img = img.resize((200, 100))
    img = ImageTk.PhotoImage(img)
    banner = Label(root, image=img)
    banner.grid(row=0, column=3, sticky=E)

    root.mainloop()

main()
