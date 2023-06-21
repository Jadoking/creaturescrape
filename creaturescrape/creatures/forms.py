from django import forms


class PokemonIngestionForm(forms.Form):
    ingestion_type = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': 'pokemon'})
    )


class DigimonIngestionForm(forms.Form):
    ingestion_type = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': 'digimon'})
    )


class OffsetIngestionForm(forms.Form):
    ingestion_type = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': 'pokemon_partial'})
    )
    offset = forms.IntegerField(min_value=0)
    limit = forms.IntegerField(min_value=1)
