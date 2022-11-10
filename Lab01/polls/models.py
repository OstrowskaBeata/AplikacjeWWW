from django.db import models

<<<<<<< Updated upstream
# Create your models here.
=======

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Person(models.Model):
    # lista wartości do wyboru w formie krotek
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # wskazanie listy poprzez przypisanie do parametru choices
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Druzyna(models.Model):
    nazwa = models.CharField(max_length=60)
    kraj = models.CharField(max_length=2)
    def __str__(self):
        return self.nazwa + " " + self.kraj


class MIESIAC(models.IntegerChoices):
    Styczen = 1
    Luty = 2
    Marzec = 3
    Kwiecien = 4
    Maj = 5
    Czerwiec = 6
    Lipiec = 7
    Sierpien = 8
    Wrzesien = 9
    Pazdziernik = 10
    Listopad = 11
    Grudzien = 12

class Osoba(models.Model):
    imie = models.CharField(max_length=60, null=False, blank=False)
    nazwisko = models.CharField(max_length=60, null=False, blank=False)
    miesiac_urodzenia = models.IntegerField(choices=MIESIAC.choices, default=timezone.now().month)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(Druzyna, null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return self.imie + " " + self.nazwisko
>>>>>>> Stashed changes
