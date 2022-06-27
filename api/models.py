from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Run(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generation = models.IntegerField(default=0)
    game = models.CharField(max_length=30)
    attempt = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)
    started_on = models.DateTimeField('date started')
    ended_on = models.DateTimeField('date ended')
    set_mode = models.BooleanField(default=False)
    dupes_clause = models.BooleanField(default=False)
    monotype = models.BooleanField(default=False)
    randomised = models.BooleanField(default=False)
    battle_items = models.BooleanField(default=False)
    level_limit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game} run: {self.attempt}"


class Pokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    nickname = models.CharField(max_length=12)
    location_encountered = models.CharField(max_length=30)
    encountered_on = models.DateTimeField('date encountered')
    caught = models.BooleanField(default=False)
    alive = models.BooleanField(default=True)
    nature = models.CharField(max_length=20)
    shiny = models.BooleanField(default=False)
    in_party = models.BooleanField(default=False)

    def __str__(self):
        return self.name
