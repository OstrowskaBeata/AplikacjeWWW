from rest_framework import serializers
from .models import Osoba, Druzyna, MIESIAC


class OsobaSerializer(serializers.Serializer):
    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)
    # pole wymagane
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=MIESIAC.choices, default=MIESIAC.choices[0][0])
    # odzwierciedlenie pola w postaci klucza obcego
    # przy dodawaniu nowego obiektu możemy odwołać się do istniejącego poprzez inicjalizację nowego obiektu
    # np. team=Team({id}) lub wcześniejszym stworzeniu nowej instancji tej klasy
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())
    data_dodania = serializers.DateField()


    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.name)
        instance.nazwisko = validated_data.get('nazwisko', instance.name)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_dodania)
        instance.druzyna = validated_data.get('druzyna', instance.team)
        instance.data_dodania = validated_data.get('data_dodania', instance.team)
        instance.save()
        return instance

class DruzynaSerializer(serializers.Serializer):
    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)
    # pole wymagane
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.name)
        instance.kraj = validated_data.get('kraj', instance.shirt_size)
        return instance