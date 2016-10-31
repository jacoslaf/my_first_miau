from django.db import models
from django.utils import timezone



class Post(models.Model):							#class to specjalne słowo kluczowe, które sygnalizuje, że tworzymy obiekt. 
    author = models.ForeignKey('auth.User')			#Post to nazwa naszego modelu. Możemy nadać mu inną nazwę (bez polskich liter,
    title = models.CharField(max_length=200)		#znaków specjalnych i spacji). Zawsze zaczynaj nazwę modelu wielką literą.
    text = models.TextField()						#models.Model oznacza, że nasz obiekt Post jest modelem Django. W ten sposób Django wie, że powinien go przechowywać w bazie danych.	
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title