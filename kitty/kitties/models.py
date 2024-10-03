from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Kitten(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    age_in_months = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Котенок'
        verbose_name_plural = 'Котята'

    def __str__(self):
        return f"{self.breed.name} - {self.color}"
