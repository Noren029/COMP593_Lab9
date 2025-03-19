# poke_api.py

import requests

def get_pokemon_info(pokemon):
    pokemon_name = str(pokemon).lower().strip()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Pokémon '{pokemon_name}' not found.")
        return None
