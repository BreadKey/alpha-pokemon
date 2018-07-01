from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Name(models.Model):
    korean = models.CharField(max_length=12, default='이름 없음')
    english = models.CharField(max_length=12, default='No name')

    def __str__(self):
        return self.korean

class Description(models.Model):
    korean = models.CharField(max_length=200, default='설명 없음')
    english = models.CharField(max_length=200, default="No description")

    def __str__(self):
        return self.korean

class PokemonType(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    super_effective_types = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)
    not_very_effective_types = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)
    ineffective_typs = models.ManyToManyField("self", blank=True, related_name='+', symmetrical=False)

    def __str__(self):
        return self.name.korean

class PokemonAbility(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class PokemonMoveCategory(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class MoveAffect(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.korean

class SecondaryEffect(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    description = models.ForeignKey(Description, on_delete=models.CASCADE, null=True)
    accuracy = models.FloatField(default=1.0)

    def __str__(self):
        return self.name.korean

class PokemonMove(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.OneToOneField(Name, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(PokemonType, on_delete=models.CASCADE, null=True)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True)
    damage = models.IntegerField(default=60)
    accuracy = models.FloatField(default=1.0)
    pp = models.IntegerField(default=5)
    max_pp = models.IntegerField(default=10)
    category = models.ForeignKey(PokemonMoveCategory, on_delete=models.SET_NULL, null=True)
    priority = models.IntegerField(default=0)
    is_contact = models.BooleanField(default=False)
    affect = models.ForeignKey(MoveAffect, on_delete=models.SET_NULL, null=True)
    affected_by_magic_coat = models.BooleanField(default=True)
    affected_by_bright_powder = models.BooleanField(default=True)
    affected_by_protect = models.BooleanField(default=True)
    affected_by_snatch = models.BooleanField(default=True)
    affected_by_kings_rock = models.BooleanField(default=True)
    secondary_effect = models.ForeignKey(SecondaryEffect, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name.korean

class Pokemon(models.Model):
    index_number = models.IntegerField(default=1)
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    base_hp = models.IntegerField(default=100)
    base_attack = models.IntegerField(default=100)
    base_defense = models.IntegerField(default=100)
    base_special_attack = models.IntegerField(default=100)
    base_special_defense = models.IntegerField(default=100)
    base_speed = models.IntegerField(default=100)
    types = models.ManyToManyField(PokemonType, blank=True)
    can_learn_moves = models.ManyToManyField(PokemonMove, blank=True)
    abilities = models.ManyToManyField(PokemonAbility, blank=True)
    hidden_ability = models.ManyToManyField(PokemonAbility, related_name='hidden_ability', blank=True)

    def __str__(self):
        return self.name.korean