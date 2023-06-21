import requests
from django.db import IntegrityError
from typing import Callable
from .models import Creature
from .enums import CreatureTypes


def ingest_creature_api(
        creature_metadata_model,
        scraper: Callable,
        **kwargs):

    data = scraper()

    new_creatures_added = 0
    for creature in data:
        creature_data = creature['creature']
        metadata = creature['metadata']
        new_creature = Creature(**creature_data)
        new_metadata = creature_metadata_model(**metadata)
        new_metadata.creature = new_creature
        try:
            new_creature.save()
            new_metadata.save()
            new_creatures_added += 1
        except IntegrityError:
            continue

    return new_creatures_added


def scrape_digimon_api():
    digimon_api_url = 'https://digimon-api.vercel.app/api/digimon'

    digimon_data = get_api_data(digimon_api_url)

    processed_data = []

    for digimon in digimon_data:
        creature_data = {
            'name': digimon['name'],
            'creature_type': CreatureTypes.DIGIMON.value,
            'img_url': digimon['img']
        }

        creature_metadata = {
            'level': digimon['level'].upper()
        }

        processed_data.append({
            'creature': creature_data,
            'metadata': creature_metadata
        })

    return processed_data


def full_scrape_pokemon_api(batches=5):
    pokemon_api_base_url = "https://pokeapi.co/api/v2/pokemon/"
    initial_grab = get_api_data(pokemon_api_base_url)
    pokemon_count = initial_grab['count']

    batch_size = pokemon_count // 5

    offset = 0

    processed_data = []

    while (offset < pokemon_count):
        batch_data = partial_scrape_pokemon_api(offset=offset,
                                                limit=batch_size)
        processed_data += batch_data

        offset += batch_size

    return processed_data


def partial_scrape_pokemon_api(offset=0, limit=100):
    pokemon_api_base_url = "https://pokeapi.co/api/v2/pokemon/"
    processed_data = []
    pokemon_batch = get_api_data(pokemon_api_base_url,
                                 offset=offset,
                                 limit=limit)
    batch = pokemon_batch['results']
    for pokemon in batch:
        pokemon_data = get_api_data(pokemon['url'])

        creature_data = {
            'name': pokemon_data['name'],
            'creature_type': CreatureTypes.POKEMON.value,
            'img_url': pokemon_data['sprites']['front_default']
        }

        pokemon_types = pokemon_data['types']

        creature_metadata = {
            'type1': pokemon_types[0]['type']['name'].upper()
        }

        if len(pokemon_types) > 1:
            creature_metadata['type2'] = pokemon_types[1][
                                         'type']['name'].upper()

        processed_data.append({
            'creature': creature_data,
            'metadata': creature_metadata
        })

    return processed_data


def get_api_data(api_url: str, **kwargs):
    query_param_string = "?" + "&".join(
                         [f'{k}={v}' for k, v in kwargs.items()]) or ""

    response = requests.get(api_url + query_param_string)

    return response.json()
