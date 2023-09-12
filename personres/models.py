from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    # Define a regex validator to allow only letters (no numbers or special characters)
    name_validator = RegexValidator(
        regex=r'^[A-Za-z\s\.]*$',  # Only allow letters and whitespace and dots
        message='Name can only contain letters and spaces.',
        code='invalid_name'
    )
    
    name = models.CharField(max_length=100, validators=[name_validator])

    def __str__(self):
        return self.name