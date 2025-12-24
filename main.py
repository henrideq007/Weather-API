from fastapi import FastAPI, HTTPException 
from services.pokemon_service import get_pokemon_data, get_random_pokemon
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI(title="Training API", version="1.0")


# Define a route to get random Pokémon data
@app.get("/pokemon/random")
def random_pokemon():
    data = get_random_pokemon()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

@app.get("/pokemon/compare")
def compare_pokemons(first: str, second: str):
    p1 = get_pokemon_data(first)
    p2 = get_pokemon_data(second)

    if not p1 or not p2:
        raise HTTPException(status_code=404, detail="One or both Pokémon not found")

    comparison = {
        "first_pokemon": {
            "name": p1["name"],
            "height": p1["height"],
            "weight": p1["weight"],
            "types": [t["type"]["name"] for t in p1["types"]]
        },
        "second_pokemon": {
            "name": p2["name"],
            "height": p2["height"],
            "weight": p2["weight"],
            "types": [t["type"]["name"] for t in p2["types"]]
        },
        "winner_by_height": p1["name"] if p1["height"] > p2["height"] else p2["name"] if p2["height"] > p1["height"] else "tie",
        "winner_by_weight": p1["name"] if p1["weight"] > p2["weight"] else p2["name"] if p2["weight"] > p1["weight"] else "tie"
    }

    return comparison


# Define a route to get Pokémon data
@app.get("/pokemon/{name}")

def read_pokemon(name: str):
    data = get_pokemon_data(name)
    if not data:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }


app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)