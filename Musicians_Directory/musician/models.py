from django.db import models

# Create your models here.
# class Instrument(models.Model):
#     instrument_name = models.CharField(max_length = 20)

#     def __str__(self):
#         return self.instrument_name


class Musician(models.Model):
    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 30)
    phone_number = models.CharField(max_length = 13)
    instrument_name = models.CharField(max_length = 20, null = True, blank = True)


    def __str__(self):
        return self.first_name
