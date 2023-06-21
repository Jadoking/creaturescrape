# Generated by Django 3.2.18 on 2023-06-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('FIRE', 'Fire'), ('WATER', 'Water'), ('GRASS', 'Grass'), ('ELECTRIC', 'Electric'), ('ICE', 'Ice'), ('FIGHTING', 'Fighting'), ('POISON', 'Poison'), ('GROUND', 'Ground'), ('FLYING', 'Flying'), ('PSYCHIC', 'Psychic'), ('BUG', 'Bug'), ('ROCK', 'Rock'), ('GHOST', 'Ghost'), ('DARK', 'Dark'), ('DRAGON', 'Dragon'), ('STEEL', 'Steel'), ('FAIRY', 'Fairy'), ('NONE', 'None')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('FIRE', 'Fire'), ('WATER', 'Water'), ('GRASS', 'Grass'), ('ELECTRIC', 'Electric'), ('ICE', 'Ice'), ('FIGHTING', 'Fighting'), ('POISON', 'Poison'), ('GROUND', 'Ground'), ('FLYING', 'Flying'), ('PSYCHIC', 'Psychic'), ('BUG', 'Bug'), ('ROCK', 'Rock'), ('GHOST', 'Ghost'), ('DARK', 'Dark'), ('DRAGON', 'Dragon'), ('STEEL', 'Steel'), ('FAIRY', 'Fairy'), ('NONE', 'None')], max_length=10),
        ),
    ]
