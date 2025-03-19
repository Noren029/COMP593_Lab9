""" COMP-593
    Scripting Lab 9
    Norlon Sibug
    10312229
    nsibug@flemingcollege.ca
""" 

from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info
from tkinter import messagebox

def main():
    root = Tk()
    root.title("Pokemon Information")

    # User input frame
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
    lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1)

    def handle_btn_get_info():
        pokemon = ent_name.get()
        poke_info = get_pokemon_info(pokemon)
        if poke_info:
            # Info
            lbl_height_val['text'] = str(poke_info['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'
        
            # Extract types properly as strings
            types = [t["type"]["name"] for t in poke_info["types"]]
            lbl_type_val["text"] = ", ".join(types)  # This will now work correctly
        
            # Stats
            bar_hp['value'] = poke_info['stats'][0]['base_stat']
            bar_attack['value'] = poke_info['stats'][1]['base_stat']
            bar_defense['value'] = poke_info['stats'][2]['base_stat']
            bar_Special_Attack['value'] = poke_info['stats'][3]['base_stat']
            bar_Special_Defense['value'] = poke_info['stats'][4]['base_stat']
            bar_Speed['value'] = poke_info['stats'][5]['base_stat']
        else:
            messagebox.showerror(message= f"I can't find this pokemon on the list {pokemon} please try again.", title="Error")

            print(f"No info received for {pokemon}.")

    
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

    lbl_Special_Attack = ttk.Label(lblfrm_stats, text="Special Attack:")
    lbl_Special_Attack.grid(row=3, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_Special_Attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_Special_Attack.grid(row=3, column=1, padx=(0, 10), pady=5)

    lbl_Special_Defense = ttk.Label(lblfrm_stats, text="Special Defense:")
    lbl_Special_Defense.grid(row=4, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_Special_Defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_Special_Defense.grid(row=4, column=1, padx=(0, 10), pady=5)

    lbl_Speed = ttk.Label(lblfrm_stats, text="Speed:")
    lbl_Speed.grid(row=5, column=0, padx=(10, 5), pady=5, sticky=E)
    bar_Speed = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
    bar_Speed.grid(row=5, column=1, padx=(0, 10), pady=5)

    root.mainloop()

main()