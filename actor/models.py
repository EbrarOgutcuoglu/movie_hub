from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


# Create your models here.
class Actor(models.Model):
    only_letters_validator = RegexValidator(
        regex=r'^[a-zA-ZçÇğĞıİöÖşŞüÜ\s]+$',
        message="you can only use letters.."
    )

    name = models.CharField(
        max_length=100,
        validators=[only_letters_validator]
    )
    photo_url = models.URLField()
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(120)
        ],
        blank=True, null=True)

    def __str__(self):
        return self.name