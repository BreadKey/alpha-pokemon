from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Name)
admin.site.register(PokemonType)
admin.site.register(PokemonAbility)
admin.site.register(Description)
admin.site.register(PokemonMove)
admin.site.register(PokemonMoveCategory)
admin.site.register(Pokemon)
admin.site.register(SecondaryEffect)
admin.site.register(MoveAffect)