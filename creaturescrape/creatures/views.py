import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from creatures.utils import (ingest_creature_api, full_scrape_pokemon_api,
                             partial_scrape_pokemon_api, scrape_digimon_api)
from creatures.models import Creature, Pokemon, Digimon
from creatures.forms import (PokemonIngestionForm, DigimonIngestionForm,
                             OffsetIngestionForm)
from creatures.enums import CreatureTypes


class CreatureView(View):
    def get(self, request):
        creature_list = Creature.objects.all()
        context = {'creature_list': creature_list}
        return render(request, 'creatures.j2', context)


class FilterCreatureView(View):
    def get(self, request, creature_type, trait, trait_value):
        if creature_type.upper() not in [types[0] for types in
                                         CreatureTypes.choices]:
            return HttpResponseBadRequest('Invalid creature type')

        creature_trait = creature_type.lower() + f'__{trait}'
        filter_params = {
                            'creature_type': creature_type.upper(),
                            creature_trait: trait_value.upper()
                        }

        try:
            creature_lists = Creature.objects.filter(**filter_params)
        except Exception:
            return HttpResponseBadRequest('Invalid trait query')

        context = {'creature_list': creature_lists}
        return render(request, 'creatures.j2', context)


class IngestionView(View):
    def get(self, request):
        pokemon_form = PokemonIngestionForm()
        digimon_form = DigimonIngestionForm()
        offset_form = OffsetIngestionForm()
        creature_count = Creature.objects.count()

        context = {
                'pokemon_form': pokemon_form,
                'digimon_form': digimon_form,
                'offset_form': offset_form,
                'creature_count': creature_count
        }
        return render(request, 'ingestion.j2', context)


class IngestDigimonView(View):
    def post(self, request):
        new_creatures_added = ingest_creature_api(Digimon, scrape_digimon_api)

        return JsonResponse({'new_creatures_added': new_creatures_added})


class IngestPokemonView(View):
    def post(self, request):
        data = None
        if request.POST:
            data = request.POST
        elif request.body:
            data = json.loads(request.body)
        scraping_function = full_scrape_pokemon_api
        partial_options = {}

        if data['ingestion_type'] == 'pokemon_partial':
            scraping_function = partial_scrape_pokemon_api
            partial_options['offset'] = data['offset']
            partial_options['limit'] = data['limit']

        new_creatures_added = ingest_creature_api(Pokemon,
                                                  scraping_function,
                                                  **partial_options)

        return JsonResponse({'new_creatures_added': new_creatures_added})
