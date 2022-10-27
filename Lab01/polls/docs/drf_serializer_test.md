# Osoba
```python
from polls.models import Osoba
from polls.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

person = Osoba(imie ='Adam', nazwisko = 'Kowalski', miesiac_urodzenia = 2)
person.save()
serializer = OsobaSerializer(person)
serializer.data
{'id': 4, 'imie': 'Adam', 'nazwisko': 'Kowalski', 'miesiac_urodzenia': 2, 'druzyna': None, 'data_dodania': '2022-10-27'}
content = JSONRenderer().render(serializer.data)
content
# output - teraz format JSON
b'{"id":4,"imie":"Adam","nazwisko":"Kowalski","miesiac_urodzenia":2,"druzyna":null,"data_dodania":"2022-10-27"}'
# w takiej formie możemy przesłać obiekt (lub cały graf obiektów) przez sieć i po "drugiej stronie" dokonać deserializacji odtwarzając graf i stan obiektów
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
#{'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'miesiac_urodzenia': ChoiceField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')], default=1), 'druzyna': PrimaryKeyRelatedField(queryset=<QuerySet [<Druzyna: Pomaranczowi PL>, <Druzyna: Czerwoni RU>, <Druzyna: Biali DE>]>), 'data_dodania': DateField()}

deserializer = OsobaSerializer(data=data)
# sprawdzamy, czy dane przechodzą walidację (aktualnie tylko domyślna walidacja, dedykowana zostanie przedstawiona na kolejnych zajęciach)
deserializer.is_valid()
# output
# False

# to oznacza pojawienie się błędu walidacji
deserializer.errors
# output
# {'team': [ErrorDetail(string='Pole nie może mieć wartości null.', code='null')]}

# w samym modelu określone są dwa atrybuty null=True, blank=True, ale jak widać serializer nie bierze tego pod uwagę
# musimy w klasie PersonSerializer zmodyfikować wartość dla pola team
# dodając atrybut allow_null=True i uruchomić całe testowanie raz jeszcze

# aby upewnić się w jaki sposób wyglądają pola wczytanego serializera/deserializera, możemy wywołać zmienną deserializer.fields, aby wyświetlić te dane
deserializer.fields

# lub
repr(deserializer)

# po powyższych zmianach walidacja powinna już się powieść
# możemy sprawdzić jak wyglądają dane obiektów po deserializacji i walidacji
deserializer.validated_data
# output
# OrderedDict([('name', 'Adam'), ('shirt_size', 'S'), ('miesiac_dodania', 1), ('team', None)])

# oraz utrwalamy dane
deserializer.save()
# sprawdzamy m.in. przyznane id
deserializer.data
```
# Druzyna

```python
from polls.models import Druzyna
from polls.serializers import DruzynaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
team= Druzyna(nazwa ='Tecza', kraj = 'UK')
team.save()
serializer = DruzynaSerializer(team)
serializer.data
{'id': 4, 'nazwa': 'Tecza', 'kraj': 'UK'}
content = JSONRenderer().render(serializer.data)
content
# output - teraz format JSON
b'{"id":4,"nazwa":"Tecza","kraj":"UK"}'
# w takiej formie możemy przesłać obiekt (lub cały graf obiektów) przez sieć i po "drugiej stronie" dokonać deserializacji odtwarzając graf i stan obiektów
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = DruzynaSerializer(data=data)
# sprawdzamy, czy dane przechodzą walidację (aktualnie tylko domyślna walidacja, dedykowana zostanie przedstawiona na kolejnych zajęciach)
deserializer.is_valid()
# output
# False

# to oznacza pojawienie się błędu walidacji
deserializer.errors
# output
# {'team': [ErrorDetail(string='Pole nie może mieć wartości null.', code='null')]}

# w samym modelu określone są dwa atrybuty null=True, blank=True, ale jak widać serializer nie bierze tego pod uwagę
# musimy w klasie PersonSerializer zmodyfikować wartość dla pola team
# dodając atrybut allow_null=True i uruchomić całe testowanie raz jeszcze

# aby upewnić się w jaki sposób wyglądają pola wczytanego serializera/deserializera, możemy wywołać zmienną deserializer.fields, aby wyświetlić te dane
deserializer.fields

# lub
repr(deserializer)

# po powyższych zmianach walidacja powinna już się powieść
# możemy sprawdzić jak wyglądają dane obiektów po deserializacji i walidacji
deserializer.validated_data
# output
# OrderedDict([('name', 'Adam'), ('shirt_size', 'S'), ('miesiac_dodania', 1), ('team', None)])

# oraz utrwalamy dane
deserializer.save()
# sprawdzamy m.in. przyznane id
deserializer.data
```