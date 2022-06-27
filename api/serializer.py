from .models import User, Run, Pokemon
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']


class RunSerializer(serializers.ModelSerializer):

    class Meta:
        model = Run
        fields = ['id', 'generation', 'game', 'attempt', 'completed', 'progress', 'started_on', 'ended_on', 'set_mode', 'dupes_clause', 'monotype', 'randomised', 'battle_items', 'level_limit', 'user']

        def to_representation(self, instance):
            self.fields['user'] = UserSerializer(read_only=True)
            return super(RunSerializer, self).to_representation(instance)


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'nickname', 'location_encountered', 'encountered_on', 'caught', 'alive', 'nature', 'shiny', 'in_party', 'run', 'user']

        def to_representation(self, instance):
            self.fields['run'] = RunSerializer(read_only=True)
            self.fields['user'] = UserSerializer(read_only=True)
            return super(PokemonSerializer, self).to_representation(instance)
