from django.db import models


class AddressModel(models.Model):
    street = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=9)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.street}, {self.city}'


class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    isAvailable = models.BooleanField()

    GENDER_CHOICES = [
        ('AN', 'Animation'),
        ('AC', 'Action'),
        ('TH', 'Thriller'),
    ]

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default='AN'
    )

    def __str__(self):
        return f'{self.title}, {self.gender}, {self.isAvailable}'


class PersonModel(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=15)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    located_movies = models.ManyToManyField(MovieModel)
    has_debits = models.BooleanField()

    def __str__(self):
        return f'{self.name}, {self.has_debits}, {self.located_movies}'
