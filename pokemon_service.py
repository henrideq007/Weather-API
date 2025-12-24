import requests
import random


POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(name: str):
    # Fetches data for a given Pokémon by name from the PokeAPI
    response = requests.get(f"{POKEAPI_URL}{name.lower()}")
    
    # Code 200 means the request was successful
    if response.status_code != 200:
        return None
    
    return response.json()

def get_random_pokemon():
    random_id = random.randint(1, 898)  # Gen 1–8 Pokémon
    response = requests.get(f"{POKEAPI_URL}{random_id}")
    if response.status_code != 200:
        return None
    return response.json()
