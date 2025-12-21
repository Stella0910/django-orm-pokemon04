from django.db import models  # noqa F401

from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    image = models.ImageField(verbose_name='Картинка', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    title_en = models.CharField(
        verbose_name='Название по-английски',
        max_length=200, blank=True
    )
    title_jp = models.CharField(
        verbose_name='Название по-японски',
        max_length=200, blank=True
    )
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционировал',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Название',
        on_delete=models.CASCADE
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    attack = models.IntegerField(verbose_name='Атака')
    defense = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon} {self.level}'
