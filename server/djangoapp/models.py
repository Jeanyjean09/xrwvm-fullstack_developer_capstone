from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # Optional: add any other relevant fields
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name  # Display car make name


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField()  # Dealer ID from Cloudant DB
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more as needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(
        default=now().year,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Show make + model
