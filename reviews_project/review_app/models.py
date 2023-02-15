from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 50, blank = False, db_index = True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length = 50, blank = False, db_index = True)
    country_key = models.ForeignKey(Country, blank = False, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length = 100, blank = False, db_index = True )
    date_production_start = models.DateField(blank = False)
    date_production_stop = models.DateField(blank = False)
    developer_key = models.ForeignKey(Developer, blank = False, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField(blank = False)
    date_created = models.DateField(auto_now_add = True)
    comment_text = models.TextField(max_length = 5000, blank = False)
    car_key = models.ForeignKey(Car, blank = False, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return f'Отзыв №{self.id} ({self.car_key.developer_key} {self.car_key}, {self.author_email})'

