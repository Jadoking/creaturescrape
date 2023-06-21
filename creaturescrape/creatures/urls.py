from django.urls import path
from . import views

app_name = 'creatures'

urlpatterns = [
    path('creature-list/', views.CreatureView.as_view(), name='creature_list'),
    path('creature-list/<str:creature_type>/<str:trait>/<str:trait_value>/',
         views.FilterCreatureView.as_view(), name='creature_filter'),
    path('', views.IngestionView.as_view(), name='ingest_page'),
    path('ingest/digimon/', views.IngestDigimonView.as_view(),
         name='ingest_digimon'),
    path('ingest/pokemon/', views.IngestPokemonView.as_view(),
         name='ingest_pokemon'),
]
