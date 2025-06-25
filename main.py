
import requests
base_url="https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url=f"{base_url}/pokemon/{pokemon_name}"
    response=requests.get(url)

    if response.status_code==200:
        pokemon_data=response.json()
        return  pokemon_data

    else:
        print(f"Failed to retreive data {response}")

    print(response)

pokemon_name="Pikachu"
pokemon_info=get_pokemon(pokemon_name)

if pokemon_info :
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")
get_pokemon(pokemon_name)

